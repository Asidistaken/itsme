import os
import sys
import argparse
from pathlib import Path
import subprocess
import logging

SUPPORTED_FORMATS = {'.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg', '.wma'}

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('volume_normalization.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def check_ffmpeg():
    try:
        subprocess.run(['ffmpeg', '-version'], 
                        capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_audio_files(folder_path):
    audio_files = []
    folder = Path(folder_path)
    
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    for file_path in folder.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_FORMATS:
            audio_files.append(file_path)
    
    return audio_files

def get_peak_volume(file_path):
    cmd = [
        'ffmpeg', '-i', str(file_path),
        '-af', 'volumedetect',
        '-f', 'null', '-'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        stderr = result.stderr
        
        # Parse max volume from ffmpeg output
        max_volume = None
        
        for line in stderr.split('\n'):
            if 'max_volume:' in line:
                max_volume = float(line.split('max_volume:')[1].split('dB')[0].strip())
                break
        
        return max_volume
    
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to analyze {file_path}: {e}")

def normalize_volume(input_path, output_path, target_db=-1.0):
    try:
        # Get current peak volume
        current_peak = get_peak_volume(input_path)
        
        if current_peak is None:
            raise Exception(f"Could not determine peak volume for {input_path}")
        
        # Calculate volume adjustment needed
        volume_adjustment = target_db - current_peak
        
        # Choose appropriate codec based on output format
        if output_path.suffix.lower() == '.mp3':
            codec_args = ['-c:a', 'libmp3lame', '-b:a', '192k']
        elif output_path.suffix.lower() == '.wav':
            codec_args = ['-c:a', 'pcm_s16le']
        elif output_path.suffix.lower() == '.flac':
            codec_args = ['-c:a', 'flac']
        elif output_path.suffix.lower() in ['.m4a', '.aac']:
            codec_args = ['-c:a', 'aac', '-b:a', '192k']
        elif output_path.suffix.lower() == '.ogg':
            codec_args = ['-c:a', 'libvorbis', '-b:a', '192k']
        else:
            codec_args = ['-c:a', 'libmp3lame', '-b:a', '192k']
        
        # Apply volume adjustment
        normalize_cmd = [
            'ffmpeg', '-i', str(input_path),
            '-af', f'volume={volume_adjustment}dB',
            *codec_args,
            '-y', str(output_path)
        ]
        
        subprocess.run(normalize_cmd, capture_output=True, check=True)
        
        return current_peak, volume_adjustment
        
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to normalize {input_path}: {e}")

def process_folder(folder_path, target_db=-1.0, output_folder=None):
    logger = logging.getLogger(__name__)
    
    if not check_ffmpeg():
        logger.error("ffmpeg is not installed or not found in PATH")
        return False
    
    try:
        audio_files = get_audio_files(folder_path)
        
        if not audio_files:
            logger.info(f"No supported audio files found in {folder_path}")
            return True
        
        logger.info(f"Found {len(audio_files)} audio files to process")
        
        # Create output folder - default to input_folder + "_normalized"
        if not output_folder:
            input_path = Path(folder_path)
            output_folder = input_path.parent / f"{input_path.name}_normalized"
        
        output_path = Path(output_folder)
        output_path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Output folder: {output_path}")
        
        processed = 0
        failed = 0
        
        for file_path in audio_files:
            try:
                logger.info(f"Processing: {file_path.name}")
                
                # Output to the designated output folder
                output_file = output_path / file_path.name
                
                # Normalize the audio
                original_peak, adjustment = normalize_volume(file_path, output_file, target_db)
                
                logger.info(f"Successfully normalized: {file_path.name} "
                        f"(was {original_peak:.1f}dB, adjusted {adjustment:+.1f}dB)")
                processed += 1
                
            except Exception as e:
                logger.error(f"Failed to process {file_path.name}: {e}")
                failed += 1
        
        logger.info(f"Processing complete. Processed: {processed}, Failed: {failed}")
        logger.info(f"All files normalized to {target_db}dB peak level")
        return True
        
    except Exception as e:
        logger.error(f"Error processing folder: {e}")
        return False

def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Normalize audio files to same peak volume level",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument('folder', help='Folder containing audio files to normalize')
    parser.add_argument('-t', '--target', type=float, default=-1.0,
                        help='Target peak dB level (default: -1.0 dB)')
    parser.add_argument('-o', '--output', help='Output folder (default: input_folder_normalized)')
    parser.add_argument('--overwrite', action='store_true',
                        help='Overwrite original files instead of creating new folder')
    
    args = parser.parse_args()
    
    # Handle output folder logic
    output_folder = args.output
    if args.overwrite:
        output_folder = args.folder  # Overwrite in same folder
    
    # Set up logging
    logger = setup_logging()
    
    logger.info(f"Starting volume normalization")
    logger.info(f"Input folder: {args.folder}")
    logger.info(f"Target peak level: {args.target} dB")
    if args.overwrite:
        logger.info(f"Output: Overwriting original files")
    else:
        logger.info(f"Output folder: {output_folder or args.folder + '_normalized'}")
    
    success = process_folder(
        args.folder,
        target_db=args.target,
        output_folder=output_folder
    )
    
    if success:
        logger.info("Volume normalization completed successfully")
        sys.exit(0)
    else:
        logger.error("Volume normalization failed")
        sys.exit(1)

if __name__ == "__main__":
    main()