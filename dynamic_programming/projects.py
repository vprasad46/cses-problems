from functools import lru_cache


@lru_cache(maxsize=512)
def find_next_job(time):
    st = 0
    en = len(projects) - 1

    while st < en:
        mid = st + (en - st)//2
        if projects[mid][0] <= time:
            st = mid + 1
        else:
            if projects[mid - 1][0] < time:
                en = mid
                break
            en = mid - 1
    return en if projects[en][0] > time else -1

@lru_cache(maxsize=512)
def doJob(index):
    if index >= len(projects):
        return 0
    #print(f"Taking job {index}")
    job_profit = projects[index][2]
    end_time = projects[index][1]
    next_job = find_next_job(end_time)
    take_job = 0
    dont_take_job = 0
    if next_job != -1:
        take_job = job_profit + doJob(next_job)
    else:
        take_job = job_profit
    dont_take_job = doJob(index+1)
    #print(f"max of {dont_take_job} and {take_job}")
    return max(dont_take_job, take_job)

if __name__ == "__main__":
    n = int(input())
    projects = []
    while n:
        st , en , profit = [int(x) for x in input().split(" ")]
        projects.append((st, en, profit))
        n -= 1
    projects.sort(key=lambda x:x[0])
    #print(projects)
    print(doJob(0))
