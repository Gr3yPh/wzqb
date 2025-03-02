const img = new Image();
img.src = 'img/whsMatrix.png';
img.onload = function() {
    const style = [
        'font-size: 1px;',
        `padding: ${this.height / 2}px ${this.width / 2}px;`,
        `background: url(${img.src}) no-repeat;`,
        'background-size: contain;'
    ].join(' ');
    console.log('%c ', style);
};