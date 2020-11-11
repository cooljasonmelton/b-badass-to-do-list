class TopicsController < ApplicationController
    def index
        render json: Topic.all, include: :todos
    end
end
