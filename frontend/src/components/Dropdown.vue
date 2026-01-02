<template>
  <div
    class="absolute right-0 top-full mt-2 w-64 bg-white border border-gray-200 rounded-lg shadow-lg z-10"
  >
    <ul class="p-2" role="menu">
      <li
        v-for="item in items"
        :key="item.id"
        @click="handleClick(item)"
        class="flex items-center p-3 mt-1 rounded-lg hover:bg-gray-100 cursor-pointer transition-colors"
        :class="{ 'bg-gray-100': selectedItem && selectedItem.id === item.id }"
      >
        <div class="flex-1">
          <div class="text-sm font-medium text-gray-900">{{ item.name }}</div>
          <div class="text-xs text-gray-500 mt-0.5">{{ item.description }}</div>
        </div>
        <svg
          v-if="selectedItem && selectedItem.id === item.id"
        class="w-5 h-5 ml-2 text-blue-600 shrink-0"
        fill="currentColor"
        viewBox="0 0 20 20"
        >
          <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
          clip-rule="evenodd"
          />
        </svg>
      </li>
    </ul>
  </div>
</template>

<script setup>
  defineProps({
    items: {
      type: Array,
      required: true
    },
    selectedItem: {
      type: Object,
      required: true
    }
  })

  const emit = defineEmits(['select', 'update:selectedItem'])

  function handleClick(item) {
    emit('select', item)
    emit('update:selectedItem', item)
  }
</script>