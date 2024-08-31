from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculator!"}

@app.get("/suma/")
def suma(operacion: str):
    try:
        operandos = operacion.split('+')
        resultado = float(operandos[0]) + float(operandos[1])
        return {"resultado": resultado}
    except (ValueError, IndexError):
        raise HTTPException(status_code=400, detail="Error en la operación")

@app.get("/resta/")
def resta(operacion: str):
    try:
        operandos = operacion.split('-')
        resultado = float(operandos[0]) - float(operandos[1])
        return {"resultado": resultado}
    except (ValueError, IndexError):
        raise HTTPException(status_code=400, detail="Error en la operación")

@app.get("/multiplicacion/")
def multiplicacion(operacion: str):
    try:
        operandos = operacion.split('*')
        resultado = float(operandos[0]) * float(operandos[1])
        return {"resultado": resultado}
    except (ValueError, IndexError):
        raise HTTPException(status_code=400, detail="Error en la operación")

@app.get("/division/")
def division(operacion: str):
    try:
        operandos = operacion.split('/')
        if float(operandos[1]) == 0:
            raise HTTPException(status_code=400, detail="Error: División por cero")
        resultado = float(operandos[0]) / float(operandos[1])
        return {"resultado": resultado}
    except (ValueError, IndexError):
        raise HTTPException(status_code=400, detail="Error en la operación")

@app.get("/borrar/")
def borrar_operacion():
    return {"resultado": ""}  # Devuelve una cadena vacía para borrar la operación