import subprocess


def main(N):
    with open("result.txt", 'w') as file:
        for i in range(N):
            rndnum = subprocess.run(["./rng.exe"], capture_output=True).stdout.decode()

            file.write(rndnum)


if __name__ == "__main__":
    N = 100000
    main(N)
