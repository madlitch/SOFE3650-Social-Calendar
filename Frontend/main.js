const { app, BrowserWindow } = require('electron');

let win;
let ready;

function createWindow () {
    win = new BrowserWindow({
        width: 1600,
        height: 900,
        minWidth: 1280,
        minHeight: 720,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    });
    win.setBackgroundColor('#000000');
}

app.on('ready', () => {
    createWindow();
    win.loadFile('index.html');
    ready = true;
});

app.on("window-all-closed", function() {
    app.quit();
});


app.allowRendererProcessReuse = false;

