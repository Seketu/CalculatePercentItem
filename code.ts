// Modern UI'yi aç
figma.showUI(__html__, { width: 450, height: 600 });

// Hesaplama fonksiyonu
function calculatePercentages() {
  const selection = figma.currentPage.selection[0];

  if (selection && selection.parent && 'height' in selection.parent && 'width' in selection.parent) {
    const frameHeight = selection.parent.height;
    const frameWidth = selection.parent.width;
    const nodeHeight = selection.height;
    const nodeWidth = selection.width;

    const heightPercent = (nodeHeight / frameHeight) * 100;
    const widthPercent = (nodeWidth / frameWidth) * 100;

    // Sonucu UI'ye gönder
    figma.ui.postMessage({
      type: 'result',
      widthPercent: widthPercent.toFixed(2),
      heightPercent: heightPercent.toFixed(2),
      nodeWidth: nodeWidth.toFixed(0),
      nodeHeight: nodeHeight.toFixed(0),
      frameWidth: frameWidth.toFixed(0),
      frameHeight: frameHeight.toFixed(0)
    });
  } else {
    // Hata mesajını UI'ye gönder
    figma.ui.postMessage({
      type: 'error',
      message: 'Lütfen bir alan seç ve parent frame içinde olduğundan emin ol.'
    });
  }
}

// İlk hesaplama
calculatePercentages();

// Seçim değiştiğinde otomatik hesapla
figma.on('selectionchange', () => {
  calculatePercentages();
});

// UI'dan gelen mesajları dinle
figma.ui.onmessage = (msg) => {
  if (msg.type === 'calculate') {
    calculatePercentages();
  } else if (msg.type === 'close') {
    figma.closePlugin();
  }
};
