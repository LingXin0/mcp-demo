import asyncio
from mcp.client import MCPClient

async def test_weather_service():
    # 连接到您的服务
    client = MCPClient(transport="stdio")
    
    # 测试获取警报功能
    print("Testing get_alerts for California:")
    alerts = await client.call("get_alerts", state="CA")
    print(alerts)
    
    # 测试获取天气预报功能
    print("\nTesting get_forecast for San Francisco:")
    forecast = await client.call("get_forecast", latitude=37.7749, longitude=-122.4194)
    print(forecast)

if __name__ == "__main__":
    asyncio.run(test_weather_service())