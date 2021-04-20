#SIMON - CIÊNCIA DE DADOS

Desenvolvimento e implementação de um Sistema de Análise e
Apresentação de Dados de Monitoramento de Condições Ambientais de
Laboratórios

O conhecimento das condições ambientais é de suma importância para a garantia da qualidade
de medição de um laboratório. Os recentes avanços em tecnologia da informação e
comunicação, que impulsionaram o paradigma de Internet das Coisas, foram facilitadores para
o desenvolvimento de redes de sensores e, em específico, a implementação de uma rede de
monitoramento para coleta de parâmetros ambientais de laboratórios. Os dados, consolidados
em um repositório de dados, precisam de adequado processamento para que a informação
relevante seja extraída e apresentada aos agentes dos laboratórios. Este projeto propõe a
implementação de um sistema de análise e apresentação dos dados coletados por uma rede
de sensores instalada nos laboratórios do Instituto Nacional de Metrologia, Qualidade e
Tecnologia (Inmetro). A informação disponibilizada permitirá o melhor controle dos parâmetros
ambientais pela geração de análises e indicadores desenvolvidos para as demandas
específicas e, em última instância, a melhora dos serviços prestados pelos laboratórios.

Objetivo Geral
O trabalho a ser desenvolvido consiste em desenvolver e implementar ferramentas de análise e
apresentação de dados relativos a parâmetros ambientais medidos por uma rede de
sensoriamento remoto instalada em laboratórios. A partir de parâmetros coletados como
temperatura, umidade e concentração de gases no ambiente, e subsequente armazenamento
em banco de dados, disponibilizar dados processados que auxiliem análises e tomadas de
decisão pelos agentes laboratoriais. Adicionalmente, modelos de predição elaborados podem
ajudar na geração de estimativas mais precisas ou na otimização dos recursos empregados no
sensoriamento.




O presente trabalho tem como base o estudo da ferramenta Elastic Search e de programação
em Python aplicada à Ciência de Dados. Os dados capturados nos laboratórios como temperatura,
umidade e a data são salvos em um formato de arquivo JSON.

Em computação,JSON , um acrônimo de JavaScript Object Notation, é um formato compacto, de padrão
aberto independente, de troca de dados simples e rápida entre sistemas, especificado 
por Douglas Crockford em 2000, que utiliza texto legível a humanos, no formato atributo-valor 
(natureza auto-descritiva). Isto é, um modelo de transmissão de informações no formato 
texto, muito usado em web services.

O código em Python que está sendo desenvolvido abrange algumas bibliotecas como a JSON, numpy,
matplotlib e time e sua função é capturar os dados salvos nos arquivos JSON, oriundos de dispositivos
instalados nos laboratórios e que utilizam sensores.	
Com isso, todas as informações referentes à temperatura, umidade e a respectiva data são salvas em 
arrays para a geração dos gráficos, que são o instrumentos capazes de nos fornecer informações relevantes.


