document.addEventListener("DOMContentLoaded", function() {
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.toString() !== "") {
        var utms = [];
        var params = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
        params.forEach(function(param) {
            if (urlParams.has(param)) {
                utms.push(urlParams.get(param));
            }
        });
        
        var utmString = utms.join('|');
        
        var links = document.querySelectorAll('a[href*="checkout.thebank.com.br"], a[href*="pay.hotmart.com"], .btn-comprar, .btn-compra');
        links.forEach(function(link) {
            try {
                if (!link.href || link.href.startsWith('#')) return;
                
                var url = new URL(link.href);
                
                // Copia todos os parametros da URL atual para o link
                urlParams.forEach(function(value, key) {
                    url.searchParams.set(key, value);
                });
                
                // Adiciona a string combinada ao sck (Origem do Afiliado)
                if (utmString) {
                    var existingSck = url.searchParams.get('sck');
                    if (existingSck) {
                        url.searchParams.set('sck', existingSck + '|' + utmString);
                    } else {
                        url.searchParams.set('sck', utmString);
                    }
                }
                
                link.href = url.toString();
            } catch (e) {
                console.error("Erro ao atualizar link de checkout:", e);
            }
        });
    }
});
