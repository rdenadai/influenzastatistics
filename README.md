# Influenza Statistics

Simple compilation and presentation of some stats about Influenza data

## Data

- FluNet by WHO: https://apps.who.int/flumart/Default?ReportNo=12

- DATASUS : ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DORES/

```python
from pysus.utilities.readdbc import read_dbc                                                                                                                     
df = read_dbc('datasets/DOSP2018.dbc', encoding='latin-1')
df[df["CAUSABAS"] == "J09"]
df[df["CAUSABAS"] == "J108"]
```

| Código         	| Descrição                                                                                                	|
|----------------	|----------------------------------------------------------------------------------------------------------	|
| CID 10 - J09   	| Influenza (gripe) devida a vírus identificado da gripe aviária                                           	|
| CID 10 - J10   	| Influenza devida a outro vírus da influenza (gripe) identificado                                         	|
| CID 10 - J10.0 	| Influenza com pneumonia devida a outro vírus da influenza (gripe) identificado                           	|
| CID 10 - J10.1 	| Influenza com outras manifestações respiratórias, devida a outro vírus da influenza (gripe) identificado 	|
| CID 10 - J10.8 	| Influenza com outras manifestações, devida a outro vírus da influenza (gripe) identificado               	|
| CID 10 - J11   	| Influenza (gripe) devida a vírus não identificado                                                        	|
| CID 10 - J11.0 	| Influenza (gripe) com pneumonia, devida a vírus não identificado                                         	|
| CID 10 - J11.1 	| Influenza (gripe) com outras manifestações respiratórias, devida a vírus não identificado                	|
| CID 10 - J11.8 	| Influenza (gripe) com outras manifestações, devida a vírus não identificado                              	|