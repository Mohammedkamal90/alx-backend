import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Create express app
const app = express();
const PORT = 1245;

// List of products
const listProducts = [
  { itemId: 1, itemName: "Suitcase 250", price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: "Suitcase 450", price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: "Suitcase 650", price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: "Suitcase 1050", price: 550, initialAvailableQuantity: 5 }
];

// Connect to Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to get item by id from listProducts
const getItemById = (id) => {
  return listProducts.find(item => item.itemId === id);
};

// Reserve stock by item id
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

// Get current reserved stock by item id
const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
};

// Route to list all products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map(item => ({
    itemId: item.itemId,
    itemName: item.itemName,
    price: item.price,
    initialAvailableQuantity: item.initialAvailableQuantity
  })));
});

// Route to get product detail by item id
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    return res.json({ status: "Product not found" });
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);
  res.json({ ...product, currentQuantity });
});

// Route to reserve product by item id
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    return res.json({ status: "Product not found" });
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity === 0) {
    return res.json({ status: "Not enough stock available", itemId });
  }
  await reserveStockById(itemId, currentQuantity - 1);
  res.json({ status: "Reservation confirmed", itemId });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
