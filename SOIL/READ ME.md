What we used AI for is a guide for making some api calls from the database.
First, set up a virtual enviroment and create a sql server with provided SQL instructions.
Provide information on a field's soil health and quality to farmers in a real-time update. These updates will occur frequently throughout the day. 



to run the server first start your venv using 
    python -m venv {venv name}
then move to the main file directory EX: (venv) {user}/SOIL
    cd {directory}
then 
    uvicorn app.main:app --reload
and go to 
    http://127.0.0.1:8000/