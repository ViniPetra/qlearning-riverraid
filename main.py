import gymnasium

env = gymnasium.make("ALE/Tetris-v5", render_mode="human", obs_type="ram")
observation, info = env.reset(seed=42)
#for _ in range(1000):
while True:
  # definição da política
  acao = env.action_space.sample()

  ambiente, recompensa, finalizado, paralizado, info = env.step(acao)
  recompensa_txt = "Recompensa: [%s]" % recompensa
  fim_txt = "Finalizado: [%s]" % finalizado
  acao_txt = "Ação: [%s]" % acao

  if (recompensa < 0):
    recompensa_txt = recompensa_txt
  elif (recompensa > 0):
    recompensa_txt = recompensa_txt

  if (finalizado):
    fim_txt = fim_txt

  print(recompensa_txt, fim_txt, acao_txt)

  if finalizado or paralizado:
    break
    #ambiente, info = env.reset()
env.close()