// TN-Keys — scripts do front-end
(function () {
    'use strict';

    // Botão "mostrar/ocultar senha"
    document.querySelectorAll('[data-toggle-password]').forEach(function (botao) {
        botao.addEventListener('click', function () {
            var campo = document.getElementById(botao.dataset.togglePassword);
            var icone = botao.querySelector('i');
            if (!campo) return;

            var mostrar = campo.type === 'password';
            campo.type = mostrar ? 'text' : 'password';
            botao.setAttribute('aria-pressed', mostrar ? 'true' : 'false');

            if (icone) {
                icone.classList.toggle('bi-eye', !mostrar);
                icone.classList.toggle('bi-eye-slash', mostrar);
            }
        });
    });

    // Evita clique duplo em formulários (duplo envio)
    document.querySelectorAll('form[data-once]').forEach(function (form) {
        form.addEventListener('submit', function () {
            var botao = form.querySelector('[type="submit"]');
            if (botao) {
                botao.disabled = true;
            }
        });
    });
})();
