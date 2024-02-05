use_bpm 130

live_loop :met1 do
  sleep 1
end

define :pattern do |pattern|
  pattern.ring.tick == "x"
end

live_loop :kick, sync: :met1 do
  a = 2
  sample :bd_haus, amp: a, release: 8, cutoff: 110 if pattern("x-----x---x--x--")
  sleep 0.25
end

live_loop :clap, sync: :met1 do
  sleep 1
  sample :perc_snap, amp: 1
  sleep 1
end

live_loop :hhc1, sync: :met1 do
  sample :drum_cymbal_closed, amp: 0.5 if pattern("x-x-x-x-xxx-x-x-")
  sleep 0.125
end

