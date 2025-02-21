document.addEventListener('DOMContentLoaded', function() {
    const socket = io();
    
    socket.on('connect', function() {
        console.log('Conectado ao servidor WebSocket');
    });

    socket.on('grade_update', function(data) {
        // Criar notificação
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.innerHTML = `
            <div class="alert alert-info alert-dismissible fade show" role="alert">
                ${data.message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;
        
        // Adicionar ao DOM
        document.body.appendChild(notification);
        
        // Remover após 5 segundos
        setTimeout(() => {
            notification.remove();
        }, 5000);

        // Se estiver na página de notas, atualizar automaticamente
        if (window.location.pathname.includes('/visualizar_notas')) {
            window.location.reload();
        }
    });
});