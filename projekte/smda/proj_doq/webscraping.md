# Webscraping

## Vorbemerkung 

Webscraping meint nicht nur das Absenden von HTTP(s)-Requests und Speichern der erhaltenen Responses, sondern das Parsen des erhaltenen Contents.

## TwIl;) [^3]
### HTML-Parsing ist eklig

Im Bereich des von uns inspizierten Teilbereiches (ehemals <var> WWW </var> genannten) Suchraumes des Internets finden sich zahlreiche Probleme für das Informationsmanagement:
- oft in Form von Markup-Sprachen[^1] - vorrangig HTML!

1. Man kommt mit "normalen" Tools wie (```sed/awk/grep/pcre/pyon re```) nicht weit(er)

2. Es benötigt Hilfe eines sog. <var>Parser</var>s (hier: [beautifulsoup4](https://pypi.org/project/beautifulsoup4/))
    -  In Unkenntnis der indiv. Struktur des Dokumentes betreiben wir also <var>Reverse Engineering</var> und lernen:
        - <u>nicht</u> wohlgeformte Dokumente (welche keine Ausnahme sind) legen Parser "auf die Nase"
            - hier können Tools wie [```HTML Tidy```](https://htmltidy.net/) helfen
        - Die Untersuchung der vorgefundenen (HTML-) Strukturen stellen uns vor das Problem: wir müssen diese untersuchen und können dann
            - a. Geeignete <var>Selektoren</var> formulieren (z.b: <kbd>div[class=foo_Bar]</kbd>)
            - b. Nicht benötigte Informationen ausfiltern


    - Das Verhältnis von Nutzdaten(Payload) zu Overhead <i>kann</I> __extrem__ ungünstig sein:
        - Größe der HTTP-Response: 538.95 KB
        - Speicherverbrauch der (für uns hier) nutzbaren Daten:  459 BYTES 
        - 459 ./. 551884,80 Bytes
        - --> Payloadload < 1‰
        - --> Overhead > 99%

Hinweis:  Exotischere Websites, deren Inhalt per ECMA-Script[^2] via JSON-Blob und zig externer Ressourcen gerendert werden, wurden hierbei nicht betrachtet


### Webscraping Beispiel Aldi Süd




```mermaid
sequenceDiagram
    autonumber
    participant Usr as User<br/>starte Script
    participant Py as Python<br/>lib requests
    participant SP as Python<br/> lib beautifulsoup4 
    participant Webserver as Aldi-Website
    Usr->>Py:python3  aldi_scrape.py  
    rect rgb(161, 241, 168)
            Py->>Webserver: HTTP Request - GET  https://filialen.aldi-sued.de/nordrhein-westfalen
            Webserver->>Py: HTTP Response - Send (HTML)
            Py-->SP: Parse HTML -> find Elemente: a[data-ya-track=todirectory]
            SP-->Py: Python Datenstruktur 
            note over Py, SP: (<class 'bs4.element.ResultSet'>)
            rect rgb(222, 86, 170)
            loop 
                SP-->Py: for item in <class 'bs4.element.ResultSet'>
                Py-->Py: get item['href'] ...
            end
    end
    end
    

```

## Datenpersistenz
```mermaid 
sequenceDiagram
    autonumber

    rect rgb(96, 98, 226)
        alt Persist(data)
            Py->>FileSystem: JSON 
        else 
            Py->>FileSystem: or CSV 
        else 
            Py->>FileSystem: or XML 
        else 
            Py->>RDBMS: or Database 
        end
    end    
```




--- 

[^1]: Meist Abkömmlinge des SGML oder XML: HTML, XHMTL oder schlimmmeres à la SOAP[^4]

[^2]: ECMA-262 ist der Standard, in welchem (sog. <var>ECMAScript</var>) -Sprachen, deren Ursprung [Javascript](https://en.wikipedia.org/wiki/JavaScript) ist, (Actionscript, JScript etc.) festgeschrieben sind

[^3]: This week I learned

[^4]: Gott sei bei uns!



