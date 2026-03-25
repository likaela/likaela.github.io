import pandas as pd
import numpy as np

def standardize_profit(raw_data: pd.DataFrame, profit_col: str = "年度收益(万元)") -> dict:
    """
    标准化企业收益：截断极端值+Min-Max归一化到-100~100
    """

    profits = raw_data[profit_col].values.astype(float)
    min_profit = profits.min()  # 原始最小值
    max_profit = profits.max()  # 原始最大值

    clipped_profits = np.clip(profits, a_min=-700, a_max=1100)

    standardized = (clipped_profits - min_profit) / (max_profit - min_profit) * 200 - 100

    node_profit = {
        name: round(float(value), 2)
        for name, value in zip(raw_data["企业名称"], standardized)
    }
    return node_profit

raw_data = pd.DataFrame({
    "企业名称": ["A公司", "B公司", "C公司", "D公司", "E公司","F公司","G公司"],
    "年度收益(万元)": [1200, -800, 500, -300, 400,1000,600]
})

node_profit = standardize_profit(raw_data)
print("运行成功！结果：")
for name, value in node_profit.items():
    print(f"{name}: {value}")
