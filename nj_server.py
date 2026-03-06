from fastapi import FastAPI, HTTPException

# Catálogo de roupas
catalog = {
    "tshirts": {
        "units": "pieces",
        "qty": 500
    },
    "jeans": {
        "units": "pieces",
        "qty": 300
    },
    "jackets": {
        "units": "pieces",
        "qty": 100
    }
}

app = FastAPI(title="Clothing Store API")

@app.get("/warehouse/{product}")
async def load_truck(product, order_qty):
    
    # Verifica se o produto existe no catálogo
    if product not in catalog:
        raise HTTPException(
            status_code=404, 
            detail="Product not found in our inventory."
        )

    order_qty_int = int(order_qty)
    
    # Trava de segurança para não negativar o estoque
    if order_qty_int > catalog[product]["qty"]:
        raise HTTPException(
            status_code=400, 
            detail=f"Sorry, only {catalog[product]['qty']} units of {product} are available."
        )
    
    # Atualiza o estoque
    catalog[product]["qty"] -= order_qty_int
    
    # Retorna o recibo
    return {
        "product": product,
        "order_qty": order_qty,
        "units": catalog[product]["units"],
        "remaining_qty": catalog[product]["qty"]
    }
