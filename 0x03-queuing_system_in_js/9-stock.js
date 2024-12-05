import express from 'express';
import { promisify } from 'util';
const redis = require('redis');

const app = express();
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
  ];

function getItemById(id) {
    return listProducts.find(product => product.id === id);
  }

app.get('/list_products', (req, res) => {
    res.json(listProducts.map(product => ({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock
    })));
  });

app.get('/list_products/:itemId', async (req, res) => {
    const product = getItemById(Number(req.params.itemId));
    if (!product) {
      return res.json({ status: 'Product not found' });
    }
  
    const reservedStock = await getAsync(`item.${product.id}`);
    const currentQuantity = product.stock - (reservedStock || 0);
  
    res.json({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
      currentQuantity
    });
  });

  async function reserveStockById(itemId, stock) {
    await setAsync(`item.${itemId}`, stock);
  }
  
  app.get('/reserve_product/:itemId', async (req, res) => {
    const product = getItemById(Number(req.params.itemId));
    if (!product) {
      return res.json({ status: 'Product not found' });
    }
  
    const reservedStock = await getAsync(`item.${product.id}`);
    const currentQuantity = product.stock - (reservedStock || 0);
  
    if (currentQuantity <= 0) {
      return res.json({ status: 'Not enough stock available', itemId: product.id });
    }
  
    await reserveStockById(product.id, (reservedStock || 0) + 1);
    res.json({ status: 'Reservation confirmed', itemId: product.id });
  });
  
  app.listen(1245, () => {
    console.log('Server running on port 1245');
  });
