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
        var sck = utms.join('|');
        
        var links = document.querySelectorAll('a[href*="checkout.thebank.com.br"], a[href*="pay.hotmart.com"]');
        links.forEach(function(link) {
            try {
                var url = new URL(link.href);
                // Copia todos os parâmetros da URL atual para o link
                urlParams.forEach(function(value, key) {
                    url.searchParams.set(key, value);
                });
                // Adiciona o sck com base nas UTMs
                if (sck) {
                    var existingSck = url.searchParams.get('sck');
                    if (existingSck) {
                        // Se já existir, junta com o novo
                        url.searchParams.set('sck', existingSck + '_' + sck);
                    } else {
                        url.searchParams.set('sck', sck);
                    }
                }
                link.href = url.toString();
            } catch (e) {
                console.error("Erro ao atualizar link de checkout:", e);
            }
        });
    }
});
