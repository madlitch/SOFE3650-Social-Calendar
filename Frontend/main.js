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
            nodeIntegration: true,
            contextIsolation: false
        }
    });
    win.setBackgroundColor('#000000');
}

app.on('ready', () => {
    createWindow();
    win.loadFile('testing.html');
    ready = true;
});

app.on("window-all-closed", function() {
    app.quit();
});


app.allowRendererProcessReuse = false;

