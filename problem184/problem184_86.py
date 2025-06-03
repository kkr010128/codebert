def main():
        S = list(input())

        ans = "No"

        if S[2]==S[3]:
                if S[4]==S[5]:
                        ans = "Yes"

        print("{}".format(ans))

if __name__=="__main__":
        main()