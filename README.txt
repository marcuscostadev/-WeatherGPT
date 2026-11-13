PROJETO: WeatherGPT com PySimpleGUI, OpenWeather, SQLite e SQLAlchemy

COMO RODAR:
1. Abra a pasta no VSCode.
2. Instale as dependências:
   pip install -r requirements.txt
3. Copie o arquivo .env.example e renomeie para .env
4. Coloque sua chave da OpenWeather:
   OPENWEATHER_API_KEY=sua_chave_aqui
5. A chave da OpenAI é opcional. Se não colocar, o sistema usa uma resposta local simples.
6. Rode:
   python main.py

O QUE O PROJETO TEM:
- Interface gráfica com PySimpleGUI
- Consulta de clima pela OpenWeather API
- Assistente virtual climática
- SQLite com SQLAlchemy
- POO
- DAO
- Arquitetura em camadas
- CRUD no histórico: criar, listar, atualizar observação e excluir
- CRUD em cidades favoritas: criar, listar, atualizar e excluir