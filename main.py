import library.process as proc
import library.filesoperations as fo





def main(step_number: int):
    if step_number == 1:
        fo.save_all_tweets_individuals()


if __name__=="__main__":
    main(1)