# Webscraping Beispiel Aldi Süd

```mermaid
sequenceDiagram
    autonumber
    participant Usr as User<br/>starte Script
    participant Py as Python<br/>lib requests
    participant SP as Python<br/> lib beautifulsoup4 
    
    participant Webserver as Overpass API
    Usr->>Py:python3 runner.py
    rect rgb(161, 241, 168)
        loop Every {TIME_INTERVAL}
            
            Py->>Webserver: HTTP Request - GET  https://filialen.aldi-sued.de/nordrhein-westfalen
            Webserver->>Py: HTTP Response - Send (HTML)
            Py-->SP: Parse HTML -> find Elemente: a[data-ya-track=todirectory]
            SP-->Py: Python Datenstruktur 
            note over Py, SP: (<class 'bs4.element.ResultSet'>)
    
        end
    end
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