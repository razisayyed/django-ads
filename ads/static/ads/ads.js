$(function() {
    var zones = [];
    $('div[data-django-ads-zone]').each(function() {
        var zone = $(this).data('django-ads-zone'); 
        zones.push(zone);
    });
    var url = Urls['ads:ad-impression']();
    $.get(url, { zones: zones }, function( data ) {
        var viewports = data.viewports;
        Object.keys(data.zones).forEach(key => {
            var $ad_container = $('div[data-django-ads-zone="'+key+'"]');
            var zone = data.zones[key];
            var html = '';
            if(zone.ad !== null) {
                ad = zone.ad;
                html = '<a href="'+ad.url+'" target="_blank">';
                Object.keys(ad['images']).forEach(key => {
                    var img = ad['images'][key];
                    html += '<img src="'+img.url+'" class="'+viewports[key]+'"/>';
                });
                html += '</a>';
                $ad_container.html(html);
            } else if ('google_adsense_slot' in zone.conf && 'google_adsense_format' in zone.conf) {
                var google_adsense_client = data.google_adsense_client;
                var google_adsense_slot = zone.conf.google_adsense_slot;
                var google_adsense_format = zone.conf.google_adsense_format;
                html = '<ins class="adsbygoogle" \
                            style="display:block" \
                            data-ad-client="'+google_adsense_client+'" \
                            data-ad-slot="'+google_adsense_slot+'" \
                            data-ad-format="'+google_adsense_format+'"></ins>';
                $ad_container.html(html);
                (adsbygoogle = window.adsbygoogle || []).push({});
            }
            if(html !== '') {
                var extra_classes = $ad_container.data('django-ads-extra-classes');
                $ad_container.addClass(extra_classes);
            }
        });
    /*
        <ins class="adsbygoogle"
        style="display:block"
        data-ad-client="{{ google_adsense_client }}"
        data-ad-slot="{{ zone.google_adsense_slot }}"
        data-ad-format="{{ zone.google_adsense_format|default:'auto' }}"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
*/
    });
    
});