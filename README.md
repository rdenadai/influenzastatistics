# Influenza Statistics

Simple compilation and presentation of some stats about Influenza data

## Data

- FluNet by WHO: https://apps.who.int/flumart/Default?ReportNo=12

- DATASUS : 
    - Dataset:
        - CID9 : ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID9/DORES/
        - CID10 : ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DORES/
    - Referência:
        - Tabela CID9 : http://tabnet.datasus.gov.br/cgi/sih/mxcid9br.htm
        - Tabela CID10 : http://tabnet.datasus.gov.br/cgi/sih/mxcid10lm.htm

| Cod. (CID 10)   | Descrição                                                                                                	|
|----------------	|----------------------------------------------------------------------------------------------------------	|
| J09   	        | Influenza (gripe) devida a vírus identificado da gripe aviária                                           	|
| J10   	        | Influenza devida a outro vírus da influenza (gripe) identificado                                         	|
| J10.0 	        | Influenza com pneumonia devida a outro vírus da influenza (gripe) identificado                           	|
| J10.1 	        | Influenza com outras manifestações respiratórias, devida a outro vírus da influenza (gripe) identificado 	|
| J10.8 	        | Influenza com outras manifestações, devida a outro vírus da influenza (gripe) identificado               	|
| J11   	        | Influenza (gripe) devida a vírus não identificado                                                        	|
| J11.0 	        | Influenza (gripe) com pneumonia, devida a vírus não identificado                                         	|
| J11.1 	        | Influenza (gripe) com outras manifestações respiratórias, devida a vírus não identificado                	|
| J11.8 	        | Influenza (gripe) com outras manifestações, devida a vírus não identificado                              	|
| J18               | Pneumonia por microorganismo não especificada
| J18.0             | Broncopneumonia não especificada
| J18.1             | Pneumonia lobar não especificada
| J18.2             | Pneumonia hipostática não especificada
| J18.8             | Outras pneumonias devidas a microorganismos não especificados
| J18.9             | Pneumonia não especificada
| U04 	            | Síndrome respiratória aguda grave (severe acute respiratory syndrome SARS)                              	|
| U04.9 	        | Síndrome respiratória aguda grave (Severe acute respiratory syndrome) (SARS), não especificada            |

---

Exemplo de código usando PySUS:

```python
from pysus.utilities.readdbc import read_dbc                                                                                                                     
df = read_dbc('datasets/DOSP2018.dbc', encoding='latin-1')
df[df["CAUSABAS"] == "J09"]
df[df["CAUSABAS"] == "J108"]
```