class ColoredSection extends HTMLElement {
constructor() {
    // Always call super first in constructor
    super();

    // Create a documentation badge
    var shadow = this.attachShadow({mode: 'open'});

    var wrapper = document.createElement('section');
    wrapper.setAttribute('data-background-image','./img/bg01.png');
    wrapper.setAttribute('data-background-size','300px');
    wrapper.setAttribute('data-background-repeat','repeat');
    wrapper.setAttribute('data-background-opacity',0.2);
    var color = this.hasAttribute('color')?this.getAttribute('color'):'#cb4b16';

    wrapper.setAttribute('data-background',color);

    shadow.appendChild(wrapper);
}
}

// register it
customElements.define('csection', ColoredSection);
