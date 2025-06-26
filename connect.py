from sqlalchemy import create_engine
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# your own connection
username = ''
password = ''
host = ''
port = ''
database = ''

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')
query = 'SELECT sleep_hours, health_score FROM health'
df = pd.read_sql(query, engine)
plt.scatter(df['sleep_hours'], df['health_score'], color='blue', alpha=0.6)
plt.title('Dependence of Health on Sleep Hours')
plt.xlabel('Sleep Hours')
plt.ylabel('Health Score')
plt.grid(True)
plt.savefig('plot.png')
