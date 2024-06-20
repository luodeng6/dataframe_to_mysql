import pandas as pd
from sqlalchemy import create_engine
# 主要代码
def dataFrameToMysql(df: pd.DataFrame, user="root", password="2002",
                     database="node_mysql", host="localhost", table_name="example_table"):
    # 创建数据库连接
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

    # 分批次插入数据
    batch_size = 100
    for i in range(0, len(df), batch_size):
        # df[i:i + batch_size].to_sql('goods_data', con=engine, if_exists='append',
        # index=False)->这是一次性插入很多，所以是replace，很可能报错
        df[i:i + batch_size].to_sql(table_name, con=engine, if_exists='append', index=False)

    # # 将 DataFrame 写入 MySQL 数据库
    # df.to_sql('goods_data', con=engine, if_exists='replace', index=False)
    print(f"DataFrame 已成功插入到 {database} 数据库中的 '{table_name}' 表。")


if __name__ == '__main__':
    file_path = "学生数据.xlsx"
    df = pd.read_excel(file_path)
    dataFrameToMysql(df, password="root", database="school", table_name="student")
