require 'ostruct'
require 'yaml'
require 'redis'
require 'sinatra'
require 'sinatra/base'

class RedWeb < Sinatra::Base
  @config_file = ARGV[0]
  @@config ||= YAML.load_file(@config_file)

  get '/' do
    erb :index, :locals => { :servers => servers }
  end

  class RedisServerInfo
    attr_reader :name
    attr_reader :host
    attr_reader :port

    def initialize(name, host, port)
      @name = name
      @host = host
      @port = port
    end

    # The Redis INFO data as a hash
    def redis_info(host, port)
      Redis.new(:host => host, :port => port).info
    end

    def master?
      info.role == "master"
    end

    def slave?
      info.role == "slave"
    end

    def slave_of
      info.master_host if slave?
    end

    def master_node
      "#{info.master_host}: #{info.master_port}"
    end

    def master_data
      {
        :role => info.role,
        :connected_slaves => info.connected_slaves,
        :slave0 => info.slave0
      }
    end

    # parse data for master, e.g:
    #   "127.1.1.1,6379,online" to
    #       {
    #         :ip     => "127.1.1.1"
    #         :port   => 6379
    #         :status => "online"
    #       }
    def connected_slave_data(data)
      arr = data.split(",")

      {
        :ip     => arr[0],
        :port   => arr[1].to_i,
        :status => arr[2]
      }
    end

    def slave_data
      {
        :role                       => info.role,
        :master_host                => info.master_host,
        :master_port                => info.master_port,
        :master_link_status         => info.master_link_status,
        :master_last_io_seconds_ago => info.master_last_io_seconds_ago,
        :master_sync_in_progress    => info.master_sync_in_progress,
        :slave_priority             => info.slave_priority,
        :slave_read_only            => info.slave_read_only,
        :connected_slaves           => info.connected_slaves
      }
    end

    # A OpenStruct object providing dot notation
    # access to the values of the Redis INFO command
    # for this server.
    def info
      @info ||= OpenStruct.new(redis_info(host, port))
    end

    def all_info
      info ||= redis_info(host, port)
      info.delete("run_id") # uninteresting
      info
    end

    def core_redis
      all_info.select { |k,v| %w(
        redis_version
        redis_git_sha1
        redis_git_dirty
        redis_mode
      ).include?(k) }
    end

    def process
      all_info.select { |k,v| %w(
        os
        multiplexing_api
        gcc_version
        process_id
        tcp_port
      ).include?(k) }
    end

    def uptime
      all_info.select { |k,v| %w(
        uptime_in_seconds
        uptime_in_days
        lru_clock
        latest_fork_usec
      ).include?(k) }
    end

    def clients
      all_info.select { |k,v| %w(
        connected_clients
        client_longest_output_list
        client_biggest_input_buf
        blocked_clients
      ).include?(k) }
    end

    def memory_and_cpu
      all_info.select { |k,v| %w(
        used_memory
        used_memory_human
        used_memory_rss
        used_memory_peak
        used_memory_peak_human
        used_memory_lua
        mem_fragmentation_ratio
        mem_allocator
        used_cpu_sys
        used_cpu_user
        used_cpu_sys_children
        used_cpu_user_children
      ).include?(k) }
    end


    def rdb
      all_info.select { |k,v| %w(
        loading
        rdb_changes_since_last_save
        rdb_bgsave_in_progress
        rdb_last_save_time
        rdb_last_bgsave_status
        rdb_last_bgsave_time_sec
        rdb_current_bgsave_time_sec
      ).include?(k) }
    end

    def aof
      all_info.select { |k,v| %w(
        aof_enabled
        aof_rewrite_in_progress
        aof_rewrite_scheduled
        aof_last_rewrite_time_sec
        aof_current_rewrite_time_sec
        aof_last_bgrewrite_status
      ).include?(k) }
    end

    def connections_and_keys
      all_info.select { |k,v| %w(
        total_connections_received
        total_commands_processed
        instantaneous_ops_per_sec
        rejected_connections
        expired_keys
        evicted_keys
        keyspace_hits
        keyspace_misses
      ).include?(k) }
    end

    def replication
      all_info.select { |k,v| %w(
        role
        master_host
        master_port
        master_link_status
        master_last_io_seconds_ago
        master_sync_in_progress
        slave_priority
        slave_read_only
        connected_slaves
        slave0
      ).include?(k) }
    end

    # Return the keys available to #info, as symbols.
    #
    # Returns an array of symbols
    def available_info_keys
      info.to_h.keys.map { |k| k.to_sym }
    end
  end

  def servers
    @@config.map do |name, data|
      RedisServerInfo.new(name, data["hostname"], data["port"])
    end
  end

  run! if app_file == $0
end
