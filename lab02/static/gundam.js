function gundamUppercaseAlpha(input) {
    const value = String(input.value || '').toUpperCase();
    input.value = value.replace(/[^A-Z]/g, '').replace(/J/g, 'I');
}

function gundamUppercaseText(input) {
    input.value = String(input.value || '').toUpperCase();
}

function gundamNormalizeNumber(input, minValue, maxValue) {
    const numericValue = Number.parseInt(input.value, 10);
    if (Number.isNaN(numericValue)) {
        return;
    }

    const bounded = Math.min(Math.max(numericValue, minValue), maxValue);
    input.value = String(bounded);
}
