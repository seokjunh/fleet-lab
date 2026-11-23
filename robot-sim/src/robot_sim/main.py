import asyncio
import aiomqtt
import json
from datetime import datetime, timezone

async def main():
    async with aiomqtt.Client("localhost") as client:
        x, y, battery = 0, 0, 100

        while True:
            msg = {}
            msg["robot_id"] = "r1"
            msg["x"] = x
            msg["y"] = y
            msg["battery"] = max(0,battery)
            msg["timestamp"] = datetime.now(timezone.utc).isoformat()

            data = json.dumps(msg)

            await client.publish("robots/r1/state", payload=data)
            await asyncio.sleep(1)

            x += 1
            y += 1
            battery -= 1

if __name__ == "__main__":
    asyncio.run(main())