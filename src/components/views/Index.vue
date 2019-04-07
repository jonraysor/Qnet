<template>
  <div class="hello">

    <div class="mb-5 search-container">
      <input id="schoolsBar"
        type="text"
        class="mb-1"
        placeholder="Search the school">
			<input id="classBar"
        type="text"
        class="mb-1"
        placeholder="Search the class">
      <div class="btn-bar">
			  <img src="@/assets/search-icon.svg" onclick="alert(schoolsBar.value)">
      </div>
    </div>

    <div class="text mb-3">
      <kbd>
        Find all your class quiz and test questions here.....
      </kbd>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Index',
  data() {
    return {
    };
  },
};
</script>

<style lang="scss" scoped>
.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;

  > input {
    width: 100%;
    height: 100%;
  }

  .btn-bar {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    align-items: flex-end;
    > img {
      cursor: pointer;
      width: 60px;
      height: 30px;
      // height: 100%;
      background-color: darkorange;
      border-radius: 5px;
      transition: all 0.3s;
    }
  }

  .text {
    kbd {
      width: 100%;
    }
  }
}

.search-container:hover > img {
  filter: contrast(200%);
}
</style>
