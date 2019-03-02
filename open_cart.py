import gym
import numpy as np
env = gym.make('CartPole-v2')

def run_episode(env, parameters):  
    observation = env.reset()
    totalreward = 0
    for _ in range(5000):
        env.render()
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

action = 1
def run(params):
	
	total_reward = run_episode(env,params)
	env.close()
	return(total_reward)
'''best_param = 0
best_reward = 0
parameters = np.random.rand(4) * 2 - 1  
for i in range(10000):
	new_param =  parameters+ (np.random.rand(4) * 2 - 1 )*0.5 
	
	if total_reward > best_reward:
		best_reward = total_reward
		best_param = parameters
		parameters  = new_param
		step = i
		if best_reward == 200:
			break;

print(step)
print(best_param)
print(best_reward)'''
#print(run(1))


