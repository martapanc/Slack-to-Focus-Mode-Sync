import subprocess


def main():
    result = subprocess.run(['shortcuts', 'run', 'Focus Mode ON'], stdout=subprocess.PIPE)
    # result = subprocess.run(['shortcuts', 'run', '--help'], stdout=subprocess.PIPE)
    print(result.stdout)


if __name__ == '__main__':
    main()
