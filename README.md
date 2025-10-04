# Como rodar o projeto:

## Passo 1: Obter chave de API do DeepSeek na OpenRouter

1. Vá para o link: e clique em `Create API Key`.
2. Crie e copie sua chave de API
3. Substitua o valor `OPENROUTER_API_KEY` pela sua chave de API
4. Coloque no `OPENROUTER_BASE_URL` o valor `https://openrouter.ai/api/v1`
5. Coloque no `OPENROUTER_MODEL` o modelo desjado, como por exemplo `deepseek/deepseek-chat-v3.1:free`

## Passo 2: Obter chave de API da OpenAI

1. Crie uma Conta na OpenAI
O primeiro passo é criar uma conta na OpenAI. Para isso, siga os passos abaixo:

Acesse o site da OpenAI .
Clique em “Sign Up” no canto superior direito da página.
Preencha os campos necessários com suas informações ou faça login utilizando sua conta do Google.

2. Acesse a Área de API Keys
Depois de criar sua conta e fazer login, você precisa acessar a área onde as API Keys são geradas:

No painel principal da OpenAI, clique em “API” no menu lateral esquerdo.
Em seguida, clique em “API Keys”.

3. Crie uma Nova API Key
Agora, vamos criar a sua API Key:

Clique no botão “Create new secret key”.
Dê um nome para a sua chave, algo que ajude você a identificá-la no futuro, como “API do curso”.
Clique em “Create secret key”.

4. Copie e Guarde sua API Key
Após criar a chave, a OpenAI exibirá o valor da sua API Key. É crucial que você copie e guarde esse valor em um lugar seguro, pois ele só será exibido uma vez. Se você perder essa chave, será necessário criar uma nova.

5. Adicione Saldo à Sua Conta
Para utilizar a API da OpenAI, você precisará adicionar saldo à sua conta. Veja como fazer isso:

No painel principal, clique em “Billing” no menu lateral esquerdo.
Clique em “Add Payment Method” e adicione um método de pagamento.
Selecione o valor que deseja adicionar (o valor mínimo é de $5, aproximadamente R$25).
Clique em “Continue” para finalizar a adição de saldo.

6. Configure Limites de Gasto
Para evitar surpresas na fatura, configure limites de gasto mensal:

Acesse a aba de limits .
Defina os limites de gastos em dólares e clique em “Save”.

7. Verifique o Uso da API
Monitore os custos gerados pela API na aba Usage . Isso ajudará você a controlar seus gastos e entender melhor como está utilizando os recursos.

### Renomeie o arquivo `.env.example` por `.env` e rode o código com `streamlit run main.py`
