# Webscraping

## Vorbemerkung 

Webscraping meint nicht nur das Absenden von HTTP(s)-Requests und Speichern der erhaltenen Responses, sondern das Parsen des erhaltenen Contents.

### HTML-Parsing ist eklig

Im Bereich des von uns inspizierten Teilbereiches (ehemals <var> WWW </var> genannten) Suchraumes des Internets finden sich zahlreiche Probleme für das Informationsmanagement:
- oft in Form von Markup-Sprachen[^1] - vorrangig HTML!

1. Man kommt mit "normalen" Tools wie (```sed/awk/grep/pcre/pyon re```) nicht weit(er)

2. Es benötigt der Hilfe eines sog. <var>Parser</var>s
    -  In Unkenntnis der indiv. Struktur des Dokumentes betreiben wir also <var>Reverse Engineering</var> und lernen:
        - <u>nicht</u> wohlgeformte Dokumente (welche keine Ausnahme sind) legen Parser "auf die Nase"
            - hier können Tools wie ```tidy``` helfen
        - Die Untersuchung der vorgefundenen (HTML-)Strukturen stellen uns vor das Problem: wir müssen diese untersuchen und können dann
            - a. Geeignete <var>Selektoren</var> formulieren
            - b. Reduntante oder nicht benötigte Informationen ausfiltern


3. Exotischere Websites, deren Inhalt per ECMA-Script[^2] via JSON-Blob und zig externer Ressourcen gerendert werden, wurden hierbei nicht betrachtet


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

[^1]: Meist Abkömmlinge des SGML oder XML: HTML, XHMTL oder schlimmmeres à la SOAP[^3]

[^2]: ECMA-262 ist der Standard, in welchem Scriptsprache deren Ursprung [Javascript](https://en.wikipedia.org/wiki/JavaScript) ist (Typescript, JScript et al.) festgeschrieben sind







[^3]:  Gott sei bei uns! 