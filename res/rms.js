const { response } = require('express');
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const { request } = require('http');
const { exit } = require('process');
const cookieParser = require("cookie-parser");
const sessions = require('express-session');
const app1 = express();
const app2 = express();
const app3 = express();
const app4 = express();
const app5 = express();
const app6 = express();
const app7 = express();
const app8 = express();
const app9 = express();
const app10 = express();
const app11 = express();
const app12 = express();
const cashdesk = express();

let db = new sqlite3.Database('test.sqlite', (err) => {
    if (err) {
        return console.error(err.message);
    }
    console.log('Connected to SQLite');
    });


currenttimestamp = 	Math.floor(new Date().getTime()/1000.0)
dago = currenttimestamp - 86400
wago = currenttimestamp - 604800
mago = currenttimestamp - 2629743

let islemalltime = `SELECT SUM(portion) AS piece, id result, timestamp FROM records WHERE timestamp < ${currenttimestamp} GROUP BY id ORDER BY piece DESC LIMIT 1;`;
db.all(islemalltime, [], (err, rows) => {
    if (err) {
        throw err;
    }
    const result = rows.map((row) => {
        return row.result;
    });
    console.log('Tüm Zamanlar',result)
    allago = result;
    });

let islemdago = `SELECT SUM(portion) AS piece, id result, timestamp FROM records WHERE timestamp < ${dago} GROUP BY id ORDER BY piece DESC LIMIT 1;`;
db.all(islemdago, [], (err, rows) => {
    if (err) {
        throw err;
    }
    const result = rows.map((row) => {
        return row.result;
    });
    console.log('dün',result)
    ddago = result;
    });

let islemwago = `SELECT SUM(portion) AS piece, id result, timestamp FROM records WHERE timestamp < ${wago} GROUP BY id ORDER BY piece DESC LIMIT 1;`;
db.all(islemwago, [], (err, rows) => {
    if (err) {
        throw err;
    }
    const result = rows.map((row) => {
        return row.result;
    });
    console.log('1 hafta önce',result)
    wwago = result;
    });

let islemmago = `SELECT SUM(portion) AS piece, id result, timestamp FROM records WHERE timestamp < ${mago} GROUP BY id ORDER BY piece DESC LIMIT 1;`;
db.all(islemmago, [], (err, rows) => {
    if (err) {
        throw err;
    }
    const result = rows.map((row) => {
        return row.result;
    });
    console.log('1 ay önce',result)
    mmago = result;
    });

let masa1_total = `SELECT SUM(portion) AS piece, id result FROM masa1 GROUP BY id ORDER BY piece;`;
let masa2_total = `SELECT SUM(portion) AS piece, id result FROM masa2 GROUP BY id ORDER BY piece;`;
let masa3_total = `SELECT SUM(portion) AS piece, id result FROM masa3 GROUP BY id ORDER BY piece;`;
let masa4_total = `SELECT SUM(portion) AS piece, id result FROM masa4 GROUP BY id ORDER BY piece;`;
let masa5_total = `SELECT SUM(portion) AS piece, id result FROM masa5 GROUP BY id ORDER BY piece;`;
let masa6_total = `SELECT SUM(portion) AS piece, id result FROM masa6 GROUP BY id ORDER BY piece;`;
let masa7_total = `SELECT SUM(portion) AS piece, id result FROM masa7 GROUP BY id ORDER BY piece;`;
let masa8_total = `SELECT SUM(portion) AS piece, id result FROM masa8 GROUP BY id ORDER BY piece;`;
let masa9_total = `SELECT SUM(portion) AS piece, id result FROM masa9 GROUP BY id ORDER BY piece;`;
let masa10_total = `SELECT SUM(portion) AS piece, id result FROM masa10 GROUP BY id ORDER BY piece;`;
let masa11_total = `SELECT SUM(portion) AS piece, id result FROM masa11 GROUP BY id ORDER BY piece;`;
let masa12_total = `SELECT SUM(portion) AS piece, id result FROM masa12 GROUP BY id ORDER BY piece;`;
/*db.all(masa1_total, [], (err, rows) => {
    if (err) {
        throw err;
    }
    const result = rows.sort((row) => {
        return row.result;
    });
    masa1_total_data = result;
    });
*/
var masa1_total_data;
var lock1 = false;
db.each(masa1_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa1_temp_data = (`${row.piece}× ${row.result}`);
    if (lock1 == false){
        masa1_total_data = masa1_temp_data;
        lock1 = true;
    }
    else{
        masa1_total_data = masa1_total_data + "\n" + masa1_temp_data
    }
});

var masa2_total_data;
var lock2 = false;
db.each(masa2_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa2_temp_data = (`${row.piece}× ${row.result}`);
    if (lock2 == false){
        masa2_total_data = masa2_temp_data;
        lock2 = true;
    }
    else{
        masa2_total_data = masa2_total_data + "\n" + masa2_temp_data
    }
});

var masa3_total_data;
var lock3 = false;
db.each(masa3_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa3_temp_data = (`${row.piece}× ${row.result}`);
    if (lock3 == false){
        masa3_total_data = masa3_temp_data;
        lock3 = true;
    }
    else{
        masa3_total_data = masa3_total_data + "\n" + masa3_temp_data
    }
});

var masa4_total_data;
var lock4 = false;
db.each(masa4_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa4_temp_data = (`${row.piece}× ${row.result}`);
    if (lock4 == false){
        masa4_total_data = masa4_temp_data;
        lock4 = true;
    }
    else{
        masa4_total_data = masa4_total_data + "\n" + masa4_temp_data
    }
});

var masa5_total_data;
var lock5 = false;
db.each(masa5_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa5_temp_data = (`${row.piece}× ${row.result}`);
    if (lock5 == false){
        masa5_total_data = masa5_temp_data;
        lock5 = true;
    }
    else{
        masa5_total_data = masa5_total_data + "\n" + masa5_temp_data
    }
});

var masa6_total_data;
var lock6 = false;
db.each(masa6_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa6_temp_data = (`${row.piece}× ${row.result}`);
    if (lock6 == false){
        masa6_total_data = masa6_temp_data;
        lock6 = true;
    }
    else{
        masa6_total_data = masa6_total_data + "\n" + masa6_temp_data
    }
});

var masa7_total_data;
var lock7 = false;
db.each(masa7_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa7_temp_data = (`${row.piece}× ${row.result}`);
    if (lock7 == false){
        masa7_total_data = masa7_temp_data;
        lock7 = true;
    }
    else{
        masa7_total_data = masa7_total_data + "\n" + masa7_temp_data
    }
});

var masa8_total_data;
var lock8 = false;
db.each(masa8_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa8_temp_data = (`${row.piece}× ${row.result}`);
    if (lock8 == false){
        masa8_total_data = masa8_temp_data;
        lock8 = true;
    }
    else{
        masa8_total_data = masa8_total_data + "\n" + masa8_temp_data
    }
});

var masa9_total_data;
var lock9 = false;
db.each(masa9_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa9_temp_data = (`${row.piece}× ${row.result}`);
    if (lock9 == false){
        masa9_total_data = masa9_temp_data;
        lock9 = true;
    }
    else{
        masa9_total_data = masa9_total_data + "\n" + masa9_temp_data
    }
});

var masa10_total_data;
var lock10 = false;
db.each(masa10_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa10_temp_data = (`${row.piece}× ${row.result}`);
    if (lock10 == false){
        masa10_total_data = masa10_temp_data;
        lock10 = true;
    }
    else{
        masa10_total_data = masa10_total_data + "\n" + masa10_temp_data
    }
});

var masa11_total_data;
var lock11 = false;
db.each(masa11_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa11_temp_data = (`${row.piece}× ${row.result}`);
    if (lock11 == false){
        masa11_total_data = masa11_temp_data;
        lock11 = true;
    }
    else{
        masa11_total_data = masa11_total_data + "\n" + masa11_temp_data
    }
});

var masa12_total_data;
var lock12 = false;
db.each(masa12_total, [], (err, row) => {
    if (err) {
        throw err;
    }
    masa12_temp_data = (`${row.piece}× ${row.result}`);
    if (lock12 == false){
        masa12_total_data = masa12_temp_data;
        lock12 = true;
    }
    else{
        masa12_total_data = masa12_total_data + "\n" + masa12_temp_data
    }
});

const oneDay = 1000 * 60 * 60 * 24;

cashdesk.use(sessions({
    secret: process.env.SESSION_SECRET,
    saveUninitialized:true,
    cookie: { maxAge: oneDay },
    resave: false
}));


cashdesk.use(express.json());
cashdesk.use(express.urlencoded({ extended: true }));

cashdesk.use(express.static(__dirname + "/kasa"));

cashdesk.use(cookieParser());

const myusername = process.env.RMS_USERNAME
const mypassword = process.env.RMS_PASSWORD

var session;

cashdesk.get('/',(req,res) => {
    session=req.session;
    if(session.userid){
        res.sendFile('kasa/index.html',{root:__dirname})
    }else
    res.sendFile('kasa/index.html',{root:__dirname})
});


cashdesk.post('/dashboard',(req,res) => {
    if(req.body.username == myusername && req.body.password == mypassword){
        session=req.session;
        session.userid=req.body.username;
        res.sendFile('login.html',{root:__dirname + "/kasa"})
    }
    else{
        res.sendFile('error.html',{root:__dirname + "/kasa"})
    }
})
/*
cashdesk.get('/dashboard', (req,res) => {
    res.json({
    masa1_total_data
    });
});*/

cashdesk.get('/dashboard', (req,res) => {
    res.json({
    all: allago,
    day: ddago,
    week: wwago,
    month: mmago,
    masa1_hesap: masa1_total_data,
    masa2_hesap: masa2_total_data,
    masa3_hesap: masa3_total_data,
    masa4_hesap: masa4_total_data,
    masa5_hesap: masa5_total_data,
    masa6_hesap: masa6_total_data,
    masa7_hesap: masa7_total_data,
    masa8_hesap: masa8_total_data,
    masa9_hesap: masa9_total_data,
    masa10_hesap: masa10_total_data,
    masa11_hesap: masa11_total_data,
    masa12_hesap: masa12_total_data,
    });
});


cashdesk.listen(2000, () => console.log ('listening at 2000 as cashdesk'));

cashdesk.get('/stfd', (request, response) => {
    request(process.exit());
});

cashdesk.get('/tc1', (request, response) => {
    db.all(`DELETE FROM masa1;`)
});
cashdesk.get('/tc2', (request, response) => {
    db.all(`DELETE FROM masa2;`)
});
cashdesk.get('/tc3', (request, response) => {
    db.all(`DELETE FROM masa3;`)
});
cashdesk.get('/tc4', (request, response) => {
    db.all(`DELETE FROM masa4;`)
});
cashdesk.get('/tc5', (request, response) => {
    db.all(`DELETE FROM masa5;`)
});
cashdesk.get('/tc6', (request, response) => {
    db.all(`DELETE FROM masa6;`)
});
cashdesk.get('/tc7', (request, response) => {
    db.all(`DELETE FROM masa7;`)
});
cashdesk.get('/tc8', (request, response) => {
    db.all(`DELETE FROM masa8;`,)
});
cashdesk.get('/tc9', (request, response) => {
    db.all(`DELETE FROM masa9;`)
});
cashdesk.get('/tc10', (request, response) => {
    db.all(`DELETE FROM masa10;`)
});
cashdesk.get('/tc11', (request, response) => {
    db.all(`DELETE FROM masa11;`)
});
cashdesk.get('/tc12', (request, response) => {
    db.all(`DELETE FROM masa12;`)
});


cashdesk.get('/bmte', (request, response) => {
    response.sendFile('test.html',{root:__dirname + "/kasa"})
});

/*cashdesk.listen(2000, () => console.log ('listening at 2000 as cashdesk'));
cashdesk.use(express.static('kasa'));
cashdesk.get('/stfd', (request, response) => {
    request(process.exit());
});
cashdesk.get('/all', (request, response) => {
    response.json(veri.row.result);
});*/

app1.listen(2001, () => console.log ('listening at 2001'));
app1.use(express.static('public'));
app1.use(express.json({limit: '1mb'}));
app1.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 1!');
    db.run("INSERT INTO masa1 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp])
});

app2.listen(2002, () => console.log ('listening at 2002'));
app2.use(express.static('public'));
app2.use(express.json({limit: '1mb'}));
app2.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 2!');
    db.run("INSERT INTO masa2 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp])
});

app3.listen(2003, () => console.log ('listening at 2003'));
app3.use(express.static('public'));
app3.use(express.json({limit: '1mb'}));
app3.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 3!');
    db.run("INSERT INTO masa3 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp])
});

app4.listen(2004, () => console.log ('listening at 2004'));
app4.use(express.static('public'));
app4.use(express.json({limit: '1mb'}));
app4.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 4!');
    db.run("INSERT INTO masa4 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp])
});

app5.listen(2005, () => console.log ('listening at 2005'));
app5.use(express.static('public'));
app5.use(express.json({limit: '1mb'}));
app5.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 5!');
    db.run("INSERT INTO masa5 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp])
});

app6.listen(2006, () => console.log ('listening at 2006'));
app6.use(express.static('public'));
app6.use(express.json({limit: '1mb'}));
app6.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 6!');
    db.run("INSERT INTO masa6 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp])
});

app7.listen(2007, () => console.log ('listening at 2007'));
app7.use(express.static('public'));
app7.use(express.json({limit: '1mb'}));
app7.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 7!');
    db.run("INSERT INTO masa7 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp])
});

app8.listen(2008, () => console.log ('listening at 2008'));
app8.use(express.static('public'));
app8.use(express.json({limit: '1mb'}));
app8.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 8!');
    db.run("INSERT INTO masa8 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp])
});

app9.listen(2009, () => console.log ('listening at 2009'));
app9.use(express.static('public'));
app9.use(express.json({limit: '1mb'}));
app9.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 9!');
    db.run("INSERT INTO masa9 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp])
});

app10.listen(2010, () => console.log ('listening at 2010'));
app10.use(express.static('public'));
app10.use(express.json({limit: '1mb'}));
app10.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 10!');
    db.run("INSERT INTO masa10 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp])
});

app11.listen(2011, () => console.log ('listening at 2011'));
app11.use(express.static('public'));
app11.use(express.json({limit: '1mb'}));
app11.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 11!');
    db.run("INSERT INTO masa11 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp])
});

app12.listen(2012, () => console.log ('listening at 2012'));
app12.use(express.static('public'));
app12.use(express.json({limit: '1mb'}));
app12.post('/api', (request, response) => {
    console.log('Something inserted to database coming from table 12!');
    db.run("INSERT INTO masa12 (portion,id) VALUES (?,?)", [request.body.porsiyon, request.body.id]);
    db.run("INSERT INTO records (portion,id,timestamp) VALUES (?,?,?)", [request.body.porsiyon, request.body.id, request.body.timestamp]);
});



/*let masa2_total = `SELECT SUM(portion) AS piece, id result FROM masa2 GROUP BY id ORDER BY piece;`;
db.all(masa2_total, [], (err, rows) => {
    if (err) {
        throw err;
    }
    rows.forEach((row) => {
        console.log(row.piece,row.result);
    });
});

let masa3_total = `SELECT SUM(portion) AS piece, id result FROM masa3 GROUP BY id ORDER BY piece;`;
db.all(masa3_total, [], (err, rows) => {
    if (err) {
        throw err;
    }
    rows.forEach((row) => {
        console.log(row.piece,row.result);
    });
});
*/

function createTable() {
    console.log("Creating Tables");
    db.run("CREATE TABLE IF NOT EXISTS masa1 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS masa2 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS masa3 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS masa4 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS masa5 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS masa6 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS masa7 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS masa8 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS masa9 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS masa10 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS masa11 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS masa12 (portion INTEGER NOT NULL, id TEXT NOT NULL)");
    db.run("CREATE TABLE IF NOT EXISTS records (portion INTEGER NOT NULL, id TEXT NOT NULL, timestamp INTEGER NOT NULL)");
}

createTable();