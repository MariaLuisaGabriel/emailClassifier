# emailClassifier

Como implementar esse projeto localmente:

## 1. Instalar os requirements em requirements.txt

```shell
pip install < requirements.txt
```

## 2. Executar o classifier.py

```shell
python classifier.py
```

## 3. Abrir o index.html no navegador

### Exemplos de entradas de email para testar o classificador:
- "Quero tirar uma dúvida quanto à nota de manutenção." Produtivo
- "Parabéns! Hoje é seu aniversário!" Improdutivo
- "Solicito esclarecimento quanto à solicitação de convites para reunião técnica" Produtivo
- "Agradeço seu comparecimento no workshop de ontem, foi de relevante engrandecimento técnico e pudemos botar os comunicados em dia" Improdutivo

## Sobre o Deploy do projeto

Quando decidi pelos modelos que implementei, as versões gratuitas de deploy não suportaram o tamanho dos dados, portanto abri mão do deploy para produção
