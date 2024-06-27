// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
//declare global {
//	namespace App {
//		// interface Error {}
//		// interface Locals {}
//		// interface PageData {}
//		// interface PageState {}
//		// interface Platform {}
//	}
//}
//
//export {};



/// 
import './styles/tailwind.css';
import App from './App.svelte';
const app = new App({
	target : document.body,
});

export default app;