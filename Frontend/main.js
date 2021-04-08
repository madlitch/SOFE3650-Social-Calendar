const { app, BrowserWindow } = require('electron');

let win;
let ready;

function createWindow () {
    win = new BrowserWindow({
        width: 1980,
        height: 1070,
        minWidth: 1000,
        minHeight: 800,
        webPreferences: {
            nodeIntegration: true
        }
    });
    win.setBackgroundColor('#000000');
}

app.commandLine.appendSwitch('js-flags', '--max-old-space-size=12288');


app.on('ready', () => {
    createWindow();
    win.loadFile('index.html');
    ready = true;
});

app.on("window-all-closed", function() {
    app.quit();
});

// app.on("activate", function() {
//     createWindow();
//     win.loadFile('index.html');
// });

app.allowRendererProcessReuse = false;
