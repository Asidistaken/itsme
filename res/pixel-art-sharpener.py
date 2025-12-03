from PIL import Image
import numpy as np
from skimage import color

#AYARLAR
min_same_neighbors = 3  # Gürültü eşiği: kaç aynı renk komşu yeterli
max_color_diff = 60     # Maksimum renk farkı (RGB) — fazla uzaksa değiştirme

#PALET (RGB)
palette_rgb = [
    (240, 110, 190),
    (195, 60, 140),
    (210, 190, 65),
    (0, 0, 0),
    (130, 185, 180),
    (180, 230, 230),
    (225, 225, 195),
    (190, 190, 150),
    (240, 220, 240),
    (190, 155, 185),
]

# PALETİ LAB'YE DÖNÜŞTÜR
palette_lab = color.rgb2lab(
    np.array(palette_rgb, dtype=np.uint8).reshape(-1, 1, 3) / 255.0
).reshape(-1, 3)

#EN YAKIN PALET RENGİ LAB'YE GÖRE
def get_closest_palette_color(rgb):
    lab = color.rgb2lab(
        np.array([[[rgb[0], rgb[1], rgb[2]]]], dtype=np.uint8) / 255.0
    )[0][0]
    distances = np.linalg.norm(palette_lab - lab, axis=1)
    closest_idx = np.argmin(distances)
    return palette_rgb[closest_idx]

#RENK FARKI (RGB)
def color_distance(c1, c2):
    return np.linalg.norm(np.array(c1) - np.array(c2))

#GÖRSELİ YÜKLE
img = Image.open("./kapi.png").convert("RGBA")
pixels = np.array(img)
height, width = pixels.shape[:2]
output_pixels = np.zeros_like(pixels)
alpha_channel = pixels[:, :, 3]

#PALET RENKLERİNE DÖNÜŞTÜR
mapped = np.zeros((height, width, 3), dtype=np.uint8)
for y in range(height):
    for x in range(width):
        if alpha_channel[y, x] == 0:
            continue
        rgb = pixels[y, x][:3]
        mapped[y, x] = get_closest_palette_color(rgb)

#GÜRÜLTÜ TEMİZLEME (KOMŞU ANALİZİ + KENAR KORUMA)
for y in range(height):
    for x in range(width):
        if alpha_channel[y, x] == 0:
            output_pixels[y, x] = (0, 0, 0, 0)
            continue

        center = tuple(mapped[y, x])

        # Kenarsa değiştir
        if y == 0 or y == height - 1 or x == 0 or x == width - 1:
            output_pixels[y, x] = (*center, 255)
            continue

        # Komşuları say
        neighbor_counts = {}
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                ny, nx = y + dy, x + dx
                if (dy != 0 or dx != 0):
                    neighbor = tuple(mapped[ny, nx])
                    neighbor_counts[neighbor] = neighbor_counts.get(neighbor, 0) + 1

        # En baskın komşu rengi
        dominant_color, count = max(neighbor_counts.items(), key=lambda kv: kv[1])

        # Değiştir veya değiştirme
        if count >= min_same_neighbors and color_distance(center, dominant_color) < max_color_diff:
            output_pixels[y, x] = (*dominant_color, 255)
        else:
            output_pixels[y, x] = (*center, 255)

#KAYDET
Image.fromarray(output_pixels.astype("uint8"), "RGBA").save("kapi-output_denoised.png")
print("✔ Görüntü başarıyla kaydedildi: output_denoised.png")
