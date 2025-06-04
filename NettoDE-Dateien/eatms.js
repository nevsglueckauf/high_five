function eaTms() {
  var _this = this;

  this.server_referrer = 'https://www.netto-online.de/filialfinder';

  this.tags_domain_mapping_id = '5';

  this.criteria_js_referrer = '';
  this.subid_js_referrer = '';
  this.publisher_js_referrer = '';
  this.admedia_js_referrer = '';
  this.zone_js_referrer = '';

  this.criteria_server_referrer = 'project';
  this.subid_server_referrer = 'subid';
  this.publisher_server_referrer = 'publisher';
  this.admedia_server_referrer = 'admedia';
  this.zone_server_referrer = '';
  
  // consent settings
  this.consent = {};
  this.consent.necessary = true;
  this.consent.statistics = true;
  this.consent.marketing = false;
  this.consent.preferences = false;

  this.session_id = '';
  

  this.rpc_url = 'https://trck.netto-online.de/trck/etms/rpc.json';
  if (this.rpc_url == '')
    this.rpc_url = '//trck.netto-online.de/trck/etms/rpc.json';

  this.triplet = '';
  this.triplet_cache = { };
  this.click_url = 'https://trck.netto-online.de/trck/eclick/{$triplet}?noredir=js';

  this.anychannel_id = '50001';

  this.seo_publisher_id = '1035';
  this.seo_project_id = '-1';

  this.referral_publisher_id = '-1';
  this.referral_project_id = '-1';

  this.is_seo = false;
  this.campaign_id = '1';

  this.touchpoint_url = '';
  this.conversiontracking_url = '';

  this.isDirectTypein = false;

  this.basketFreeze = localStorage.getItem('eamTrck_BasketFreeze');
  this.localTime = parseInt(new Date() / 1000);

  
  

  this.init = function () {
    if(typeof eaTmsDocumentReferrer !== 'undefined') {
        this.referrer = eaTmsDocumentReferrer;
    } else {
	this.referrer = document.referrer;
    }
    this.href = window.location.href;
    this.referrer_get = this.getParams(this.referrer);
    this.server_referrer_get = this.getParams(this.server_referrer);
    this.href_get = this.getParams(this.href);

    if (typeof (sessionStorage) !== 'undefined' && sessionStorage.s_eamSessionId && sessionStorage.s_eamSessionId.length == 24) {
      this.session_id = sessionStorage.s_eamSessionId;
    } else if (typeof localStorage !== 'undefined' && localStorage.getItem('ls_eamSessionId') && localStorage.getItem('ls_eamSessionId').length == 24) {
      this.session_id = localStorage.getItem('ls_eamSessionId');
    }

    if (typeof sessionStorage !== 'undefined') {
      sessionStorage.s_eamSessionId = this.session_id;
    }

    if (typeof localStorage !== 'undefined') {
      localStorage.setItem('ls_eamSessionId', this.session_id);
    }
  };

  this.getReferrer = function() {
    return this.referrer;
  }

  this.setReferrer = function(referrer) {
    this.referrer = referrer;
    this.referrer_get = this.getParams(this.referrer);
  }

  this.getCookie = function (cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') c = c.substring(1);
      if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
  };

    this.insertAndExecute = function (id, text) {
        domelement = document.getElementById(id);
        domelement.innerHTML = text;

        var scripts = [];
        ret = domelement.childNodes;

        var ret = Array.prototype.slice.call(ret);

        for (var i = 0; i < ret.length; i++) {
            if (scripts && _this.nodeName(ret[i], "script")) {
                var src = '';
                if (typeof ret[i].src != 'undefined') {
                    var src = ret[i].src;
                }
                var javascript = ret[i].parentNode ? ret[i].parentNode.removeChild(ret[i]) : ret[i];
                scripts.push({src: src, javascript: javascript});

            }
        }

        for (script in scripts) {
            _this.evalScript(scripts[script]);
        }
    }

    this.nodeName = function (elem, name) {
        return elem.nodeName && elem.nodeName.toUpperCase() === name.toUpperCase();
    }

    this.evalScript = function (domelem) {
        var elem = domelem.javascript;
        if (typeof elem == 'undefined') {
            return false;
        }

        data = ( elem.text || elem.textContent || elem.innerHTML || "" );

        var head = document.getElementsByTagName("head")[0] || document.documentElement,
            script = document.createElement("script");
        script.type = "text/javascript";

        script.appendChild(document.createTextNode(data));
        if (domelem.src != '') {
            script.src = domelem.src;
        }
        head.insertBefore(script, head.firstChild);
/*        head.removeChild(script);*/

        if (elem.parentNode) {
/*            elem.parentNode.removeChild(elem);*/
        }
    }

  this.getParams = function (addr) {
    var params = new Array();
    if (addr.indexOf('?') !== -1) {
      addr = addr.split('?')[1].split('&');
      for (var i = 0; i < addr.length; i++) {
        var item = addr[i].split('=');
        if (item[0])
          params[item[0]] = (item[1]) ? item[1] : "";
      }
    } else if (addr.indexOf('#') !== -1) {
      addr = addr.split('#')[1].split('&');
      for (var i = 0; i < addr.length; i++) {
        var item = addr[i].split('=');
        if (item[0])
          params[item[0]] = (item[1]) ? item[1] : "";
      }
    }
    return params;
  };

  this.runByJsReferrer = function () {
    if (typeof this.href_get[this.criteria_js_referrer] !== 'undefined') {
      this.tripletCriteria = this.href_get[this.criteria_js_referrer];
    } else {
      return false;
    }

    if (typeof this.referrer_get[this.subid_js_referrer] !== 'undefined') {
      this.subid = this.referrer_get[this.subid_js_referrer];
    } else if (typeof this.href_get[this.subid_js_referrer] !== 'undefined') {
      this.subid = this.href_get[this.subid_js_referrer];
    }

    if (typeof this.referrer_get[this.publisher_js_referrer] !== 'undefined') {
      this.publisher = this.referrer_get[this.publisher_js_referrer];
    } else if (typeof this.href_get[this.publisher_js_referrer] !== 'undefined') {
      this.publisher = this.href_get[this.publisher_js_referrer];
    }

    if (typeof this.referrer_get[this.admedia_js_referrer] !== 'undefined') {
      this.admedia = this.referrer_get[this.admedia_js_referrer];
    } else if (typeof this.href_get[this.admedia_js_referrer] !== 'undefined') {
      this.admedia = this.href_get[this.admedia_js_referrer];
    }

    if (typeof this.referrer_get[this.zone_js_referrer] !== 'undefined') {
      this.zone = this.referrer_get[this.zone_js_referrer];
    } else if (typeof this.href_get[this.zone_js_referrer] !== 'undefined') {
      this.zone = this.href_get[this.zone_js_referrer];
    }

    return true;
  };

  this.runByServerReferrer = function () {
    if (typeof this.server_referrer_get[this.criteria_server_referrer] !== 'undefined') {
      this.tripletCriteria = this.server_referrer_get[this.criteria_server_referrer];
    } else {
      return false;
    }

    if (typeof this.server_referrer_get[this.subid_server_referrer] !== 'undefined') {
      this.subid = this.server_referrer_get[this.subid_server_referrer];
    }

    if (typeof this.server_referrer_get[this.publisher_server_referrer] !== 'undefined') {
      this.publisher = this.server_referrer_get[this.publisher_server_referrer];
    }

    if (typeof this.server_referrer_get[this.admedia_server_referrer] !== 'undefined') {
      this.admedia = this.server_referrer_get[this.admedia_server_referrer];
    }

    if (typeof this.server_referrer_get[this.zone_server_referrer] !== 'undefined') {
      this.zone = this.server_referrer_get[this.zone_server_referrer];
    }

    return true;
  };

  this.registerClick = function (triplet, replaceQuestionmark) {
    if (this.click_url != '') {
      this.click_url = this.click_url.replace('{$triplet}', triplet);
      this.click_url = this.click_url.replace('{$ref}', encodeURIComponent(this.referrer));
      this.click_url = this.click_url.replace('{$session_id}', this.session_id);

      if (typeof this.subid !== 'undefined') {
        var subid_url = '&subid=' + encodeURIComponent(this.subid);
      } else {
        var subid_url = '';
      }

      if (typeof this.publisher !== 'undefined') {
        var publisher_url = '&publisher=' + this.publisher;
      } else {
        var publisher_url = '';
      }

      if (typeof this.admedia !== 'undefined') {
        var admedia_url = '&admedia=' + this.admedia;
      } else {
        var admedia_url = '';
      }

      if (typeof this.zone !== 'undefined') {
        var zone_url = '&zone=' + this.zone;
      } else {
        var zone_url = '';
      }

      var params = this.getParams(window.location.href);
      if (typeof this.session_id !== 'undefined' && this.session_id != '' && this.session_id.length == 24) {
        var trs_url = '&trs=' + this.session_id;
      } else if (typeof params['emid'] !== 'undefined' && params['emid'] != '' && params['emid'].length == 24) {
        var trs_url = '&trs=' + params['emid'];
      } else {
        var trs_url = '';
      }

      if (typeof this.server_referrer !== 'undefined' && this.server_referrer != '') {
        var referrer_url = '&ref=' + encodeURIComponent(this.server_referrer);
      } else {
        var referrer_url = '';
      }

      if (typeof replaceQuestionmark !== 'undefined' && replaceQuestionmark == true) {
        var nth = 0;
        var url = this.click_url.replace(/\?/g, function (match, i, original) {
          nth++;
          return (nth === 2) ? "&" : match;
        });
        this.getScript(url + subid_url + publisher_url + admedia_url + trs_url + referrer_url + zone_url);
      } else {
        this.getScript(this.click_url + subid_url + publisher_url + admedia_url + trs_url + referrer_url + zone_url);
      }
    }
  }

  this.registerTouchpoint = function () {
    if (this.touchpoint_url != '') {
      this.touchpoint_url = this.touchpoint_url.replace('{$referrer}', encodeURIComponent(this.referrer));
      this.touchpoint_url = this.touchpoint_url.replace('{$session_id}', this.session_id);
      this.getScript(this.touchpoint_url);
    }
  }

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

  this.serialize = function (obj, prefix) {
    var str = [];
    for (var p in obj) {
      if (obj.hasOwnProperty(p)) {
        var k = prefix ? prefix + "[" + p + "]" : p, v = obj[p];
        str.push(typeof v == "object" ?
          this.serialize(v, k) :
          encodeURIComponent(k) + "=" + encodeURIComponent(v));
      }
    }
    return str.join("&");
  }

  this.getJSON = function (path, data, success, error) {
    var xhr = new XMLHttpRequest();
    path = path + '?' + this.serialize(data);
    xhr.onreadystatechange = function () {
      if (
        (typeof XMLHttpRequest.DONE !== 'undefined' && xhr.readyState === XMLHttpRequest.DONE) ||
        xhr.readyState === 4
      ) {
        if (xhr.status === 200) {
          if (success)
            success(JSON.parse(xhr.responseText));
        } else {
          if (error)
            error(xhr);
        }
      }
    };
    xhr.open("GET", path, true);
    xhr.send();
  }

  this.getTriplet = function () {
    if (typeof this.tripletCriteria !== 'undefined') {
      var cache_criteria = this.tripletCriteria.trim().replace(' ', '');
      if (typeof this.triplet_cache[cache_criteria] != 'undefined') {
        this.registerClick(this.triplet_cache[cache_criteria]);
      } else {
        var tripletData = {
          triplet: this.tripletCriteria              
        };

        if(typeof this.publisher !== 'undefined' && this.publisher !== '') {
          tripletData.publisher = this.publisher;
        }
        
        this.getJSON(
          this.rpc_url,
          {
            function: 'getTriplet',
            data: tripletData,
            campaign_id: this.campaign_id
          },
          function (data) {
            eaTms.registerClick(data.triplet);
          }
        );
      }
    } else if (this.getCookie('trs') != '') {
      this.registerTouchpoint();
    }
  };

  this.runTracking = function () {
    if (this.conversiontracking_url != '') {
      var params = this.getParams(window.location.href);
      if (typeof basketOrderUUID != 'undefined' && basketOrderUUID != 'undefined' && basketOrderUUID != '') {
        this.conversiontracking_url = this.conversiontracking_url.replace('{$token}', basketOrderUUID);
        this.conversiontracking_url = this.conversiontracking_url.replace('{$ref}', encodeURIComponent(window.location.href));
        this.getScript(this.conversiontracking_url);
      } else if (typeof params['pagetype'] != 'undefined' && params['pagetype'] == 'checkout_step_thanks' && params['OrderID'] != '') {
        this.conversiontracking_url = this.conversiontracking_url.replace('{$token}', params['OrderID']);
        this.conversiontracking_url = this.conversiontracking_url.replace('{$ref}', encodeURIComponent(window.location.href));
        this.getScript(this.conversiontracking_url);
      } else if (typeof params['OrderID'] != 'undefined' && params['OrderID'] != '') {
        var source = $('head').html();
        var token = source.slice(source.search('basketOrderUUID'), source.indexOf(';', source.search('basketOrderUUID'))).split('="')[1].replace('"', '').trim();
        this.conversiontracking_url = this.conversiontracking_url.replace('{$token}', token);
        this.conversiontracking_url = this.conversiontracking_url.replace('{$ref}', encodeURIComponent(window.location.href));
        this.getScript(this.conversiontracking_url);
      }
    }
  };

  this.registerTrackingByReferrer = function (referrer) {
    this.getJSON(
      this.rpc_url,
      {
        function: 'getTripletByReferrer',
        data: {
          referrer: referrer
        }
      },
      function (data) {
        eaTms.registerClick(data.triplet);
      }
    );
  };

  this.isSearchReferrer = function (referrer) {
    return referrer.match(/^(https|http):\/\/www\.google\./g)
      || referrer.match(/^(http|https):\/\/www\.bing\./g)
      || referrer.match(/^(http|https):\/\/www\.yahoo\./g)
      || referrer.match(/^(http|https):\/\/www\.ecosia\./g)
      || referrer.match(/^(http|https):\/\/www\.baidu\./g)
      || referrer.match(/^(http|https):\/\/www\.duckduckgo\./g)
      || referrer.match(/^(http|https):\/\/www\.yandex\./g)
      || referrer.match(/^(http|https):\/\/www\.fireball\./g)
      || referrer.match(/^(http|https):\/\/www\.web\./g)
      || referrer.match(/^(http|https):\/\/www\.metager\./g)
      ;
  };

  this.runByDirectTypeIn = function () {
    eaTms.registerClick('?campaign_id=' + this.campaign_id + '&project_id=' + this.anychannel_id + '&admedia_alias=default&easy_admedia_type=default&clicktype=first_click&noredir=js&timestamp=' + Date.now() + '&subid=' + encodeURIComponent(this.referrer), true);
  };

  this.runByReferral = function () {
    if(typeof this.server_referrer !== 'undefined' && this.server_referrer !== '') {
      var serverReferrer = new URL(this.server_referrer).hostname.split(".").slice(-2)[0];
    } else {
      var serverReferrer = '';
    }
    if (typeof this.referrer !== 'undefined' && this.referral_publisher_id > 0 && this.referrer !== '') {
      var jsReferrer = new URL(this.referrer).hostname.split(".").slice(-2)[0];      
      var projectAlias = new URL(this.referrer).hostname.split(".").slice(-2).join('.');      
      if (serverReferrer !== jsReferrer) {
        eaTms.registerClick('?campaign_id=' + this.campaign_id + '&publisher_id=' + this.referral_publisher_id + '&project_alias=' + projectAlias + '&admedia_alias=default&easy_admedia_type=default&clicktype=referral_click&noredir=js&timestamp=' + Date.now(), true);
      }
    } else if (typeof this.referrer !== 'undefined' && this.referrer !== '' && this.referral_project_id > 0) {
      var jsReferrer = new URL(this.referrer).hostname.split(".").slice(-2)[0];      
      if (serverReferrer !== jsReferrer) {
        eaTms.registerClick('?campaign_id=' + this.campaign_id + '&project_id=' + this.referral_project_id + '&admedia_alias=default&easy_admedia_type=default&subid=' + encodeURIComponent(this.referrer) + '&clicktype=referral_click&noredir=js&timestamp=' + Date.now(), true);
      }
    } 
  }

  this.runBySEO = function () {
    // run by seo and publisher id
    if (this.seo_publisher_id > 0 && this.isSearchReferrer(this.referrer)) {
      this.is_seo = true;
      var seoURL = new URL(this.referrer).hostname.split(".").slice(-2).join(".");
      eaTms.registerClick('?campaign_id=' + this.campaign_id + '&publisher_id=' + this.seo_publisher_id + '&project_alias=' + seoURL + '&admedia_alias=default&easy_admedia_type=default&clicktype=seo_click&noredir=js&timestamp=' + Date.now() + '&subid=' + encodeURIComponent(this.referrer), true);
      return true;
    }

    // run by seo and project id
    if (this.seo_project_id > 0 && this.isSearchReferrer(this.referrer)) {
      this.is_seo = true;
      eaTms.registerClick('?campaign_id=' + this.campaign_id + '&project_id=' + this.seo_project_id + '&admedia_alias=default&easy_admedia_type=default&clicktype=seo_click&noredir=js&timestamp=' + Date.now() + '&subid=' + encodeURIComponent(this.referrer), true);
      return true;
    }
    return false;
  };

  this.run = function () {
    if (typeof this.basketFreeze == null || this.localTime > this.basketFreeze) {
      if (this.criteria_js_referrer != '') {
        if (this.runByJsReferrer() == false) {
          if (this.runBySEO() == false) {
            this.runByReferral();
          }

          if (this.isDirectTypein)
            this.runByDirectTypeIn();
        }
      }

      if (this.criteria_server_referrer != '') {
        if (this.runByServerReferrer() == false) {
          this.runBySEO();
          if (this.session_id == '')
            this.runByDirectTypeIn();
        }
      }

      this.triplet = this.getTriplet();
      this.runTracking();
    }
  };

  this.reRun = function () {
    if (this.criteria_js_referrer != '') {
      this.runByJsReferrer();
    }
    this.triplet = this.getTriplet();
    this.runTracking();
  };

  this.reloadTags = function (options) {
    if (options.consent == true) {
      var url = '//trck.netto-online.de/trck/etms/eatms.js?disable_tags=true&campaign_id=1&referrer=https%3A%2F%2Fwww.netto-online.de%2Ffilialfinder';
      url = url.replace('&disable_tags=true', '');
      url = url.replace('?disable_tags=true', '');
      this.getScript(url);
    }
  };

  this.sendTouchpoint = function (type = "", value = "", additional = [], additionalGet = null) {
    if (type.length === 0) {
      return false;
    }

    var querystring = "";
    querystring += "?type=" + encodeURIComponent(type);

    if (value.length > 0) {
      querystring += "&value=" + encodeURIComponent(value);
    }

    var encodedAdditional = {};
    for (key in additional) {
      if (typeof (additional[key]) === "string") {
        additional[key] = encodeURIComponent(additional[key]);
      }
      encodedAdditional[key] = additional[key];
    }



    if (Object.keys(encodedAdditional).length > 0) {
      querystring += "&additional=" + JSON.stringify(encodedAdditional);
    }

    querystring += "&campaign_id=" + this.campaign_id + "&language=" + navigator.language;

    if (typeof window.product == 'object') {
      querystring += "&dynamicadditionals=" + JSON.stringify(window.product);
    }

    if (additionalGet !== null) {
    	querystring += '&' + Object.keys(additionalGet).map(function(k) {return encodeURIComponent(k) + '=' + encodeURIComponent(additionalGet[k])}).join('&');
    }

    var touchpoint_url = "https://trck.netto-online.de/trck/etp/" + querystring;

    if (typeof fetch === 'function') {
      fetch(touchpoint_url, {
        method: "GET",
        keepalive: true,
        credentials: "include"
      });
    } else {
      this.getScript(touchpoint_url);
    }
  }

}

var eaTmsTriggers = {
  addListenOn(listenerObject, executeFunction, trigger = 'click') {
    if (typeof(listenerObject) === 'object' && typeof(listenerObject.addEventListener) === 'function') {
      listenerObject.addEventListener(trigger, executeFunction);
    }
  },
  delListenOn(listenerObject, executeFunction, trigger = 'click') {
    if (typeof(listenerObject) === 'object' && typeof(listenerObject.addEventListener) === 'function') {
      listenerObject.removeEventListener(trigger, executeFunction);
    }
  }
}

function eaConvSys() {
  this.etrack_url = '//trck.netto-online.de/trck/etrack/';
  this.init = function () {

  };

  this.serializeObj = function (obj) {
    var str = '';
    for (var key in obj) {
      if (str != "") {
        str += "&";
      }
      str += key + "=" + encodeURIComponent(obj[key]);
    }
    return str;
  };

  this.addConversion = function (data) {
    var url = this.etrack_url + '?' + this.serializeObj(data);

    eaTms.getScript(url, function () {
    });
  };
}


if (typeof eaTms == 'function') {
  var eaTms = new eaTms();
  eaTms.init();
  eaTms.run();
}

if (typeof eaConvSys == 'function') {
  var eaConvSys = new eaConvSys();
  eaConvSys.init();
}

(function () {
  var getKey = 'emid'
  var storageKey = 'emid'
  var getValue = getParameterByName(getKey)
  if (getValue) {
    window.localStorage.setItem(storageKey, getValue)
  }
  function getParameterByName(e, n) { n || (n = window.location.href), e = e.replace(/[\[\]]/g, "\\$&"); var r = new RegExp("[?&]" + e + "(=([^&#]*)|&|#|$)").exec(n); return r ? r[2] ? decodeURIComponent(r[2].replace(/\+/g, " ")) : "" : null }
})();

(function () {
  var getKey = 'aaaid';
  var storageKey = 'aaaid';

  var aaaCookieExpirationDays = 60;
  var aaaCookieKey = 'aaaid';
  var re = /\.([^\.]+?)\.([^\.]+?)$/;
  var aaaCookieDomain = re.exec(location.hostname);

  if (aaaCookieDomain != null) {
    aaaCookieDomain = aaaCookieDomain[0];
  } else {
    var re = /\.([^\.]+?)$/;
    var aaaCookieDomain = re.exec(location.hostname);
    if (aaaCookieDomain != null)
      aaaCookieDomain = aaaCookieDomain[0];
  }

  var getValue = getParameterByName(getKey);

  if (getValue) {
    window.localStorage.setItem(storageKey, getValue);
    setAAACookie(aaaCookieKey, getValue, aaaCookieExpirationDays, aaaCookieDomain);
  } else {
    if (!window.localStorage.getItem(storageKey) && getCookie(aaaCookieKey)) {
      window.localStorage.setItem(storageKey, getCookie(aaaCookieKey));
    }
  }

  function setAAACookie(cname, cvalue, exdays, cdomain) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/;SameSite=none;domain=" + cdomain + ";Secure;";
  }

  function getCookie(e) { for (var n = e + "=", t = decodeURIComponent(document.cookie).split(";"), o = 0; o < t.length; o++) { for (var r = t[o]; " " == r.charAt(0);)r = r.substring(1); if (0 == r.indexOf(n)) return r.substring(n.length, r.length) } return "" }
  function getParameterByName(e, n) { n || (n = window.location.href), e = e.replace(/[\[\]]/g, "\\$&"); var r = new RegExp("[?&]" + e + "(=([^&#]*)|&|#|$)").exec(n); return r ? r[2] ? decodeURIComponent(r[2].replace(/\+/g, " ")) : "" : null }
})();

(function () {
  var getKey = 'emid';
  var storageKey = 'emid';

  var emidCookieExpirationDays = 60;
  var emidCookieKey = 'emid';
  var emidCookieDomain = 'Subdomain';

  var re = /\.([^\.]+?)\.([^\.]+?)$/;
  var emidCookieDomain = re.exec(location.hostname);

  if (emidCookieDomain != null) {
    emidCookieDomain = emidCookieDomain[0];
  } else {
    var re = /\.([^\.]+?)$/;
    var emidCookieDomain = re.exec(location.hostname);
    if (emidCookieDomain != null)
      emidCookieDomain = emidCookieDomain[0];
  }

  var getValue = getParameterByName(getKey);
  if (getValue) {
    window.localStorage.setItem(storageKey, getValue);
    setEmidCookie(emidCookieKey, getValue, emidCookieExpirationDays, emidCookieDomain);
  }

  function setEmidCookie(cname, cvalue, exdays, cdomain) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "Expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";Path=/;SameSite=none;Domain=" + cdomain + ";Secure";
  }

  function getParameterByName(e, n) { n || (n = window.location.href), e = e.replace(/[[]]/g, "\$&"); var r = new RegExp("[?&]" + e + "(=([^&#]*)|&|#|$)").exec(n); return r ? r[2] ? decodeURIComponent(r[2].replace(/\+/g, " ")) : "" : null }
})();
