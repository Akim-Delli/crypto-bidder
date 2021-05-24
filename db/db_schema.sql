CREATE TABLE cryptocurrencies (
  id int(11) NOT NULL AUTO_INCREMENT,
  coingecko_id VARCHAR(36),
  name VARCHAR(24),
  symbol VARCHAR(6),
  current_price FLOAT,
  market_cap BIGINT,
  ownership INTEGER DEFAULT 0,
  spent FLOAT DEFAULT 0.0,
  portfolio_value FLOAT AS (ownership * current_price),
  gain_loss FLOAT AS (portfolio_value - spent),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

,
  PRIMARY KEY ( id ),
  UNIQUE(symbol)
)
