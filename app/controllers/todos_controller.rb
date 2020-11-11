class TodosController < ApplicationController
    def create
        todo = Todo.create(name: params[:name], text: params[:text], importance: params[:importance], topic_id: params[:topicId])
        render json: Topic.all, include: :todos
    end
end

