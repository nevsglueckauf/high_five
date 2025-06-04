function eaTmsReferrer() {
    this.getScript = function (source, callback) {
        var script = document.createElement('script');
        var prior = document.getElementsByTagName('script')[0];
        script.async = 1;
        prior.parentNode.insertBefore(script, prior);

        script.onload = script.onreadystatechange = function (_, isAbort) {
            if (isAbort || !script.readyState || /loaded|complete/.test(script.readyState)) {
                script.onload = script.onreadystatechange = null;
                script = undefined;

                if (!isAbort) {
                    if (callback) callback();
                }
            }
        };

        script.src = source;
    }
    this.run = function() {
        var etmsUrl = 'https://trck.netto-online.de/trck/etms/eatms.js?disable_tags=true&campaign_id=1&referrer=' + encodeURIComponent(window.location.href);
        eaTmsReferrer.getScript(etmsUrl);
    }
}

var eaTmsReferrer = new eaTmsReferrer();
eaTmsReferrer.run();