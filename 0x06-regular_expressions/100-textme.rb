#!/usr/bin/env ruby

sender = ARGV[0].scan(/\[from:([^\[\]]*)\]/).flatten.first
receiver = ARGV[0].scan(/\[to:([^\[\]]*)\]/).flatten.first
flags = ARGV[0].scan(/\[flags:([^\[\]]*)\]/).flatten.first

if sender && receiver && flags
  puts "#{sender}, #{receiver}, #{flags}"
end
