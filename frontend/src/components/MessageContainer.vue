<template>
  <main class="flex-1 overflow-y-auto">
      <div class="max-w-3xl mx-auto px-6 py-8">
        <ChatEmptyState v-if="messages.length === 0" />
        <div v-else class="space-y-6">
          <div
            v-for="message in messages"
            :key="message.id"
            class="group"
            @mouseenter="hoveredMessageId = message.id"
            @mouseleave="hoveredMessageId = null"
          >
            <UserMessageCard
              v-if="message.role === 'user'"
              v-model:message="message.content"
            />
            <ModelMessageCard
              v-else-if="message.role === 'ai'"
              :content="message.content"
              :model="message.model"
            />
          </div>
        </div>
      </div>
    </main>
</template>

<script setup>
  import { ref } from 'vue'
  import { storeToRefs } from 'pinia'
  import { useChatStore } from "../store/chat"

  import ChatEmptyState from './ChatEmptyState.vue'
  import UserMessageCard from './UserMessageCard.vue'
  import ModelMessageCard from './ModelMessageCard.vue'

  const { messages, selectedModel } = storeToRefs(useChatStore())

  const hoveredMessageId = ref(null)
  const isLoading = ref(true)
</script>
