from mcp.server.fastmcp import FastMCP

# 创建 MCP 服务器实例
mcp = FastMCP("我的工具集")

# -------- 工具 1：天气查询 --------
@mcp.tool()
def get_weather(city: str) -> str:
    """获取指定城市的天气信息
    
    Args:
        city: 城市名称，如"北京"
    """
    # 这里可以替换为真实天气 API 调用
    return f"{city} 的天气：晴，25°C，湿度 60%"


# -------- 工具 2：计算器 --------
@mcp.tool()
def calculate(expression: str) -> float:
    """计算数学表达式
    
    Args:
        expression: 数学表达式，如 "2 + 3 * 4"
    """
    # 注意：生产环境建议用更安全的方式替代 eval
    return eval(expression)


# -------- 工具 3：文本反转（第三个工具，满足实验要求） --------
@mcp.tool()
def reverse_text(text: str) -> str:
    """反转输入的文本
    
    Args:
        text: 要反转的文本
    """
    return text[::-1]


# 启动服务器
if __name__ == "__main__":
    mcp.run(transport="stdio")